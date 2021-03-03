# Technology Radar rendering

Creating a way to use github for managing and rendering technology radars

## The Idea

- check in structured files to github containing info on technology, its classification, description, etc.
- have a one-page app that can point at a folder containing said files and render a technology radar from them

Can use the Issue Tracking in github for requests to alter the info. Can use github Projects to track work needed to update content. Can use branches and pull requests to maintain publication versions (current/next/etc.)

## Status

> **RESEARCH**

_Code should not be relied upon as it has not been test-driven. It is entirely for exploring whether this idea might work. Use at your own risk._

## Thanks

Borrowed and/or adapted code from the following places, with thanks:

- [Zalando](http://zalando.de)  [`github`](https://github.com/zalando/tech-radar) : adapted their 3djs renderer - [`radar.js`](https://github.com/zalando/tech-radar/tree/master/docs/radar.js) - which is used on their public technology radar [Zalando Tech
Radar](http://zalando.github.io/tech-radar/)
  
## License

```
The MIT License (MIT)

Copyright (c) 2021 John S. Nolan (stigmergist)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```