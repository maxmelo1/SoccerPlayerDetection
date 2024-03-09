_base_ = './tood_r50_fpn_1x_soccer.py'
max_epochs = 300

# learning rate
param_scheduler = [
    dict(
        type='LinearLR', start_factor=0.001, by_epoch=False, begin=0, end=500),
    dict(
        type='MultiStepLR',
        begin=0,
        end=max_epochs,
        by_epoch=True,
        milestones=[16, 22],
        gamma=0.1)
]

# training schedule for 2x
train_cfg = dict(max_epochs=max_epochs)

# multi-scale training
train_pipeline = [
    dict(type='LoadImageFromFile', backend_args={{_base_.backend_args}}),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='RandomResize', scale=[(1280, 600), (1280, 600)],
        keep_ratio=True),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PackDetInputs')
]
train_dataloader = dict(
    batch_size=8,
    num_workers=2,
    dataset=dict(pipeline=train_pipeline)
    )
