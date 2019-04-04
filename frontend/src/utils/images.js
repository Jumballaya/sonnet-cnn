class Camera {
  constructor(w, h) {
    this.w = w;
    this.h = h;
    this.video = this.makeVideo();
    this.canvas = this.makeCanvas();
    this.ctx = this.canvas.getContext('2d');
    this.stream = null;
    this.hasCamera =
      navigator.mediaDevices && navigator.mediaDevices.getUserMedia;
  }

  makeVideo() {
    const v = document.createElement('video');
    v.setAttribute('width', this.w);
    v.setAttribute('height', this.h);
    return v;
  }

  makeCanvas() {
    const c = document.createElement('canvas');
    c.setAttribute('width', this.w);
    c.setAttribute('height', this.h);
    return c;
  }

  async activateCamera() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    this.stream = stream;
    this.video.srcObject = this.stream;
    return this.video.play();
  }

  async capture() {
    await this.activateCamera();
    this.ctx.drawImage(this.video, 0, 0, this.w, this.h);
    const data = this.ctx.getImageData(0, 0, this.w, this.h);
    return new Promise((resolve, reject) => {
      this.canvas.toBlob(img => resolve(img), 'image/jpeg');
    });
  }
}

const dataToString = imagedata => {
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  canvas.width = imagedata.width;
  canvas.height = imagedata.height;
  ctx.putImageData(imagedata, 0, 0);
  return canvas.toDataURL();
};

const fileToString = file =>
  new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = e => resolve(e.target.result);
    reader.readAsDataURL(file);
  });

const parseImageSrc = async src => {
  if (typeof src === 'string') return src;
  if (src instanceof ImageData) return dataToString(src);
  if (src instanceof File || src instanceof Blob)
    return await fileToString(src);
  return '';
};

export { Camera, dataToString, fileToString, parseImageSrc };
