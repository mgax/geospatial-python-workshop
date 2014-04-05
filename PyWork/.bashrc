export GISBASE="/usr/lib/grass64"
export PATH="$PATH:$GISBASE/bin:$GISBASE/script:$GISBASE/lib"
export PYTHONPATH="${PYTHONPATH}:$GISBASE/etc/python/"
export PYTHONPATH="${PYTHONPATH}:$GISBASE/etc/python/grass"
export PYTHONPATH="${PYTHONPATH}:$GISBASE/etc/python/grass/script"
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$GISBASE/lib"
export GIS_LOCK=$$
export GISRC="$HOME/.grassrc6"
