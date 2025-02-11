Building OpenCV.js by Emscripten
====================

[Download and install Emscripten](https://emscripten.org/docs/getting_started/downloads.html).

Custom Build
------------

1. Modify `opencv_js.config.py` for custom build.

2. Set up emsdk

```shell
~/emsdk/emsdk install latest
~/emsdk/emsdk activate latest
. ~/emsdk/emsdk_env.sh
```

3. Run build

```shell
emcmake python ./platforms/js/build_js.py ./build/custom_wasm --config ./opencv_repo/opencv/platforms/js/opencv_js.config.py --build_wasm --disable_single_file --build_flags="-O3" --clean_build_dir
```

**Optional params: `simd`, `threads`**

```shell
emmake python ./platforms/js/build_js.py ./opencv_repo/build_wasm --simd --threads ...
```

**Build flags:**

* --closure 1 can be added in  to minify Emscripten-generated JS code (--build_flags="... --closure 1")
* -O3 good setting for a release build (--build_flags="... -O3")
* -g1 Controls the level of debuggability (--build_flags="... -g1")

If everything is fine, a few minutes later you will get `<build_dir>/bin/opencv.js`. You can add this into your web pages.
