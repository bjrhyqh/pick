#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/cyr/catkin_ur/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/cyr/catkin_ur/install/lib/python2.7/dist-packages:/home/cyr/catkin_ur/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/cyr/catkin_ur/build" \
    "/usr/bin/python" \
    "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/setup.py" \
    build --build-base "/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/grasp" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/cyr/catkin_ur/install" --install-scripts="/home/cyr/catkin_ur/install/bin"
