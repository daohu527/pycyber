## pycyber dependencies
Pycyber depends on the cyber library of c++, in order to install successfully, you need to depend on the following shard libraries.

1. Modify build opt in `third_party/fastrtps/fastcdr.BUILD` and `third_party/fastrtps/fastrtps.BUILD`.
```starlark
cc_library(
    name = "fastcdr",
    includes = [
        ".",
    ],
    linkopts = [
        "-L/usr/local/fast-rtps/lib",
        "-lfastcdr",
        "-Wl,-rpath,$$ORIGIN/fastrtps", # add rpath
    ],
    visibility = ["//visibility:public"],
)
```

2. Rename `fastrtps.so` and `libfastcdr.so` to `fastrtps.so.1` and `libfastcdr.so.1`

3. Copy cyber wrapper shared library in `cyber/python/internal`
