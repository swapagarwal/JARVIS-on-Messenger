hook_dir=".git/hooks"
tracked_dir="bin/git-hooks"
hook_name="$1"

yell() { echo "$0: $*" >&2; }
die() { yell "$*"; exit 111; }
try() { "$@" || die "cannot $*"; }

if [ ! -d ".git" ]; then
   echo 'You must run this script from the root dir of a `git` project' >&2
   exit 1
fi

if [ -z "$hook_name" ]; then
   usage="usage: $(basename "$0") hookname"
   echo "$usage"
   exit
fi

if [ ! -h "$hook_dir/$requested_hook" -a -x "$hook_dir/$hook_name" ]; then
	try mv "$hook_dir/$hook_name" "$hook_dir/$hook_name.local"
fi

rm "$hook_dir/$hook_hame" 2>/dev/null

tracked_path="$tracked_dir/$hook_name"
if [ ! -x "$tracked_path" ]; then exit 0; fi

hook_path="$hook_dir/$(basename "$tracked_path")"
if [ -L "$hook_path" ]; then
	rm $hook_path
fi
echo $(ln -s "../../$tracked_path" "$hook_path")
