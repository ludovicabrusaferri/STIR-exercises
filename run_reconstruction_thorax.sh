#! /bin/sh -e

cp EX_reconstruction/* working_folder/single_slice/

cd working_folder/single_slice/

../../run_reconstructions.sh

cd ../..
