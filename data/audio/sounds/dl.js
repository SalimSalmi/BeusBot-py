var fs = require('fs');
var youtubedl = require('youtube-dl');
var video = youtubedl('https://www.youtube.com/watch?v=5edkoUo36wk',
  // Optional arguments passed to youtube-dl.
  ['--format=18'],
  // Additional options can be given for calling `child_process.execFile()`.
  { cwd: __dirname });

// Will be called when the download starts.
video.on('info', function(info) {
  console.log('Download started');
  console.log('filename: ' + info.filename);
  console.log('size: ' + info.size);
});

video.pipe(fs.createWriteStream('myvideo.mp4'));

c.r = c.r + (255 - c.a * i * sampleStep) + samples[i].r * i * sampleStep;

c.r = c.r + samples[i].r * samples[i].a * (1 - c.a);
c.g = c.g + samples[i].g * samples[i].a * (1 - c.a);
c.b = c.b + samples[i].b * samples[i].a * (1 - c.a);

c.a = c.a + samples[i].a * (1 - c.a);
