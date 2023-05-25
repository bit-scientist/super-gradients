# TODO: It would be nice to create keys here as: make_pretrained_model_key(Models.RESNET18, Dataset.COCO)
# TODO: Not only this would reduce risk of making a typo error, it would bring more clarity how the key is created
# TODO: And allow to "query" pretrained models by dataset
MODEL_URLS = {
    "regnetY800_imagenet": "https://sghub.deci.ai/models/regnetY800_imagenet.pth",
    "regnetY600_imagenet": "https://sghub.deci.ai/models/regnetY600_imagenet.pth",
    "regnetY400_imagenet": "https://sghub.deci.ai/models/regnetY400_imagenet.pth",
    "regnetY200_imagenet": "https://sghub.deci.ai/models/regnetY200_imagenet.pth",
    "resnet50_imagenet": "https://sghub.deci.ai/models/resnet50_imagenet.pth",
    "resnet34_imagenet": "https://sghub.deci.ai/models/resnet34_imagenet.pth",
    "resnet18_imagenet": "https://sghub.deci.ai/models/resnet18_imagenet.pth",
    "repvgg_a0_imagenet": "https://sghub.deci.ai/models/repvgg_a0_imagenet.pth",
    "shelfnet34_lw_coco_segmentation_subclass": "https://sghub.deci.ai/models/shelfnet34_lw_coco_segmentation_subclass.pth",
    "ddrnet_23_cityscapes": "https://sghub.deci.ai/models/ddrnet_23_cityscapes.pth",
    "ddrnet_23_slim_cityscapes": "https://sghub.deci.ai/models/ddrnet_23_slim_cityscapes.pth",
    "ddrnet_39_cityscapes": "https://sghub.deci.ai/models/ddrnet_39_cityscapes.pth",
    "stdc1_seg50_cityscapes": "https://sghub.deci.ai/models/stdc1_seg50_cityscapes.pth",
    "stdc1_seg75_cityscapes": "https://sghub.deci.ai/models/stdc1_seg75_cityscapes.pth",
    "stdc2_seg50_cityscapes": "https://sghub.deci.ai/models/stdc2_seg50_cityscapes.pth",
    "stdc2_seg75_cityscapes": "https://sghub.deci.ai/models/stdc2_seg75_cityscapes.pth",
    "efficientnet_b0_imagenet": "https://sghub.deci.ai/models/efficientnet_b0_imagenet.pth",
    "ssd_lite_mobilenet_v2_coco": "https://sghub.deci.ai/models/ssd_lite_mobilenet_v2_coco.pth",
    "ssd_mobilenet_v1_coco": "https://sghub.deci.ai/models/ssd_mobilenet_v1_coco.pth",
    "mobilenet_v3_large_imagenet": "https://sghub.deci.ai/models/mobilenet_v3_large_imagenet.pth",
    "mobilenet_v3_small_imagenet": "https://sghub.deci.ai/models/mobilenet_v3_small_imagenet.pth",
    "mobilenet_v2_imagenet": "https://sghub.deci.ai/models/mobilenet_v2_imagenet.pth",
    "regseg48_cityscapes": "https://sghub.deci.ai/models/regseg48_cityscapes.pth",
    "vit_base_imagenet21k": "https://sghub.deci.ai/models/vit_base_imagenet21k.pth",
    "vit_large_imagenet21k": "https://sghub.deci.ai/models/vit_large_imagenet21k.pth",
    "vit_base_imagenet": "https://sghub.deci.ai/models/vit_base_imagenet.pth",
    "vit_large_imagenet": "https://sghub.deci.ai/models/vit_large_imagenet.pth",
    "beit_base_patch16_224_imagenet": "https://sghub.deci.ai/models/beit_base_patch16_224_imagenet.pth",
    "beit_base_patch16_224_cifar10": "https://sghub.deci.ai/models/beit_base_patch16_224_cifar10.pth",
    "yolox_s_coco": "https://sghub.deci.ai/models/yolox_s_coco.pth",
    "yolox_m_coco": "https://sghub.deci.ai/models/yolox_m_coco.pth",
    "yolox_l_coco": "https://sghub.deci.ai/models/yolox_l_coco.pth",
    "yolox_t_coco": "https://sghub.deci.ai/models/yolox_t_coco.pth",
    "yolox_n_coco": "https://sghub.deci.ai/models/yolox_n_coco.pth",
    "pp_lite_t_seg50_cityscapes": "https://sghub.deci.ai/models/pp_lite_t_seg50_cityscapes.pth",
    "pp_lite_t_seg75_cityscapes": "https://sghub.deci.ai/models/pp_lite_t_seg75_cityscapes.pth",
    "pp_lite_b_seg50_cityscapes": "https://sghub.deci.ai/models/pp_lite_b_seg50_cityscapes.pth",
    "pp_lite_b_seg75_cityscapes": "https://sghub.deci.ai/models/pp_lite_b_seg75_cityscapes.pth",
    "ppyoloe_s_coco": "https://sghub.deci.ai/models/ppyoloe_s_coco.pth",
    "ppyoloe_m_coco": "https://sghub.deci.ai/models/ppyoloe_m_coco.pth",
    "ppyoloe_l_coco": "https://sghub.deci.ai/models/ppyoloe_l_coco.pth",
    "ppyoloe_x_coco": "https://sghub.deci.ai/models/ppyoloe_x_coco.pth",
    "yolo_nas_s_coco": "https://sghub.deci.ai/models/yolo_nas_s_coco.pth",
    "yolo_nas_m_coco": "https://sghub.deci.ai/models/yolo_nas_m_coco.pth",
    "yolo_nas_l_coco": "https://sghub.deci.ai/models/yolo_nas_l_coco.pth",
    "dekr_w32_no_dc_coco_pose": "https://sghub.deci.ai/models/coco2017_pose_dekr_w32_no_dc.pth",
    "pose_rescoring_coco_coco_pose": "https://sghub.deci.ai/models/pose_rescoring_coco_coco_pose.pth",
    # These weights are here for transfer learning purpose for YOLO-NAS pose training
    # We use detection weights as initialization for pose estimation model
    "yolo_nas_pose_s_coco": "https://sghub.deci.ai/models/yolo_nas_s_coco.pth",
    "yolo_nas_pose_m_coco": "https://sghub.deci.ai/models/yolo_nas_m_coco.pth",
    "yolo_nas_pose_l_coco": "https://sghub.deci.ai/models/yolo_nas_l_coco.pth",
}


PRETRAINED_NUM_CLASSES = {
    "imagenet": 1000,
    "imagenet21k": 21843,
    "coco_segmentation_subclass": 21,
    "cityscapes": 19,
    "coco": 80,
    "coco_pose": 17,
    "cifar10": 10,
}
