import md
import os
import sys

if os.path.exists('cu.traj'):
    os.unlink('cu.traj')

md.run_md()

if not os.path.exists('cu.traj'):
    sys.exit(1)
