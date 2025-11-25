source /lustre/fs12/portfolios/nvr/users/ymingli/miniconda3/etc/profile.d/conda.sh
conda activate gaussian_splatting
torchrun --standalone --nnodes=1 --nproc-per-node=8 /lustre/fs12/portfolios/nvr/projects/nvr_av_end2endav/users/ymingli/projects/mhb/citygaussian/Grendel-GS/train.py --bsz 8 -s /lustre/fsw/portfolios/nvr/users/ymingli/datasets/supermarket/Supermarket/sample_3_process -m /lustre/fs12/portfolios/nvr/projects/nvr_av_end2endav/users/ymingli/projects/mhb/citygaussian/Grendel-GS/sample_3 --iteration 200000 --eval
