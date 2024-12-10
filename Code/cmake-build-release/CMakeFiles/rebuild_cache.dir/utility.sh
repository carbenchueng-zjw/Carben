set -e

cd /cygdrive/d/1-Git/cmake-build-release
/cygdrive/c/Users/38268/AppData/Local/JetBrains/CLion2024.2/cygwin_cmake/bin/cmake.exe --regenerate-during-build -S$(CMAKE_SOURCE_DIR) -B$(CMAKE_BINARY_DIR)
