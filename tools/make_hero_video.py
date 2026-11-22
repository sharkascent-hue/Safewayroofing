# Usage: python3 tools/make_hero_video.py assets/video/hero.mp4 <folder-of-original-photos>
# Smooth Ken Burns: float-precision affine crops per frame, piped raw to ffmpeg.
import subprocess, sys, math
from PIL import Image, ImageOps
I = sys.argv[2].rstrip('/') + '/'  # folder holding the full-size original photos
OUT = sys.argv[1]
W, H, FPS, D, X = 1280, 720, 25, 5.0, 1.0
# (file, zoom_start, zoom_end, (cx0,cy0)->(cx1,cy1) focus as fraction of image)
shots = [
 ("safeway-rooing-van.jpeg",                         1.00, 1.08, (0.50,0.52),(0.50,0.52)),
 ("project-img-roofers-laying-underlay.webp",        1.10, 1.02, (0.50,0.50),(0.50,0.50)),
 ("project-img-white-fascia-soffit-gutter-house.webp",1.08,1.08, (0.42,0.50),(0.58,0.50)),
 ("project-img-roof-relay-before-after-01.webp",     1.00, 1.07, (0.50,0.45),(0.50,0.50)),
 ("project-img-gable-chimney-fascia-gutter.webp",    1.08, 1.08, (0.58,0.48),(0.42,0.48)),
 ("project-img-black-fascia-soffit-gutter-render.webp",1.10,1.02,(0.50,0.50),(0.50,0.50)),
 ("safeway-rooing-van.jpeg",                         1.08, 1.00, (0.50,0.52),(0.50,0.52)),
]
def ease(t): return 0.5 - 0.5*math.cos(math.pi*t)  # smooth start and stop
# preload: cover-fit each image to 2x output (2560x1440) for supersampled quality
imgs = []
for f,*_ in shots:
    im = ImageOps.exif_transpose(Image.open(I+f)).convert('RGB')
    imgs.append(ImageOps.fit(im, (W*2, H*2), Image.LANCZOS))
def frame(k, t):
    im = imgs[k]; _, z0, z1, c0, c1 = shots[k]
    e = ease(min(max(t/D,0),1))
    z = z0 + (z1-z0)*e
    cx = (c0[0] + (c1[0]-c0[0])*e) * im.width
    cy = (c0[1] + (c1[1]-c0[1])*e) * im.height
    cw, ch = im.width/z, im.height/z
    x0 = min(max(cx-cw/2, 0), im.width-cw); y0 = min(max(cy-ch/2, 0), im.height-ch)
    s = cw / W  # source pixels per output pixel (float, so motion is sub-pixel)
    return im.transform((W, H), Image.AFFINE, (s, 0, x0, 0, s, y0), resample=Image.BICUBIC)
step = D - X
total = int(round((step*(len(shots)-1) + D) * FPS))
p = subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
   '-an','-c:v','libx264','-preset','slow','-crf','26','-maxrate','1000k','-bufsize','2000k','-pix_fmt','yuv420p','-profile:v','high',
   '-tune','film','-movflags','+faststart', OUT], stdin=subprocess.PIPE)
for n in range(total):
    T = n / FPS
    k = min(int(T // step), len(shots)-1)
    t = T - k*step
    f = frame(k, t)
    if t > step and k+1 < len(shots):        # crossfade into next shot
        f = Image.blend(f, frame(k+1, t-step), (t-step)/X)
    p.stdin.write(f.tobytes())
p.stdin.close(); p.wait(); print('frames', total, 'rc', p.returncode)
