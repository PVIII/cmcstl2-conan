#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(archs=["x86_64"], build_types=["Debug"], docker_run_options='--cap-add SYS_PTRACE')
    builder.add_common_builds()
    builder.run()
