# profile_collection

This repo offers a ipython profile for running tests of the XPD stack.


## Install
To install this clone this repo under your ``.ipython`` directory.

If you don't have the XPD stack installed please install it with
``conda install xpdacq xpdan -c conda-forge`` following all subsequent prompts.
You can check your install by running ``image_to_iq -- --help`` in any directory.

## Running
Make certain that all servers are running before you start the profile.

In seperate terminals activate the conda environment with the xpd stack
and run:
- ``bluesky-0MQ-proxy 5567 5568 -vvv``
- ``analysis_server``
- ``save_server``
- ``viz_server``
- and any other servers you need (see xpdAn docs for a full listing of servers)

Once these servers are running then run (in the xpd stack env) ``ipython --profile=collection``.

