from dataclasses import dataclass
from typing import Optional


@dataclass
class Brand:
    """Brand information dataclass"""

    id: str
    name: str
    gsmarena_link: str
    number_of_devices: int


@dataclass
class Device:
    """Contains data that is displayed on the brand's devices page at **gsmarena**"""

    title: str
    extended_title: str
    img_link: str
    gsmarena_link: str


@dataclass
class DeviceDetails:
    """Contains data that is displayed on header content of the device's page at **gsmarena**"""

    model_name: str
    img_link: str
    released: str
    body: str | None = None
    os: str | None = None
    storage: str | None = None
    display_size: str | None = None
    display_res: str | None = None
    camera_pixels: str | None = None
    camera_pixel_unit: str | None = None
    video_pixels: str | None = None
    ram_size: str | None = None
    ram_size_unit: str | None = None
    chipset: str | None = None
    battery_size: str | None = None
    battery_size_unit: str | None = None
    battery_type: str | None = None


@dataclass
class DeviceSpecs:
    """Contains the device's specs listed on the device's page at **gsmarena**"""

    model_name: str
    img_link: str
    comment: Optional[str] = None
    network_technology: Optional[str] = None
    network_speed: Optional[str] = None
    launch_announced: Optional[str] = None
    launch_status: Optional[str] = None
    body_dimensions: Optional[str] = None
    body_weight: Optional[str] = None
    body_build: Optional[str] = None
    body_sim: Optional[str] = None
    body_other: Optional[str] = None
    display_type: Optional[str] = None
    display_size: Optional[str] = None
    display_resolution: Optional[str] = None
    display_protection: Optional[str] = None
    display_other: Optional[str] = None
    platform_os: Optional[str] = None
    platform_chipset: Optional[str] = None
    platform_cpu: Optional[str] = None
    platform_gpu: Optional[str] = None
    memory_card_slot: Optional[str] = None
    memory_internal: Optional[str] = None
    memory_other: Optional[str] = None
    main_camera_type: Optional[str] = None
    main_camera_specs: Optional[str] = None
    main_camera_features: Optional[str] = None
    main_camera_video: Optional[str] = None
    selfie_camera_type: Optional[str] = None
    selfie_camera_specs: Optional[str] = None
    selfie_camera_features: Optional[str] = None
    selfie_camera_video: Optional[str] = None
    comms_wlan: Optional[str] = None
    comms_bluetooth: Optional[str] = None
    comms_gps: Optional[str] = None
    comms_nfc: Optional[str] = None
    comms_radio: Optional[str] = None
    comms_usb: Optional[str] = None
    features_sensors: Optional[str] = None
    features_other: Optional[str] = None
    battery_type: Optional[str] = None
    misc_colors: Optional[str] = None
    misc_models: Optional[str] = None
    misc_price: Optional[str] = None
