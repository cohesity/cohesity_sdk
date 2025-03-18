# coding: utf-8

"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recover_gpfs_to_gpfs_volume_target_params import RecoverGpfsToGpfsVolumeTargetParams
from cohesity_sdk.cluster.models.recover_nas_volume_to_view_params import RecoverNasVolumeToViewParams
from cohesity_sdk.cluster.models.recover_other_nas_to_elastifile_volume_target_params import RecoverOtherNasToElastifileVolumeTargetParams
from cohesity_sdk.cluster.models.recover_other_nas_to_flashblade_volume_target_params import RecoverOtherNasToFlashbladeVolumeTargetParams
from cohesity_sdk.cluster.models.recover_other_nas_to_generic_nas_volume_target_params import RecoverOtherNasToGenericNasVolumeTargetParams
from cohesity_sdk.cluster.models.recover_other_nas_to_isilon_volume_target_params import RecoverOtherNasToIsilonVolumeTargetParams
from cohesity_sdk.cluster.models.recover_other_nas_to_netapp_volume_target_params import RecoverOtherNasToNetappVolumeTargetParams
from typing import Set
from typing_extensions import Self

class RecoverGpfsNasVolumeParams(BaseModel):
    """
    Specifies the parameters to recover GPFS NAS volumes.
    """ # noqa: E501
    elastifile_target_params: Optional[RecoverOtherNasToElastifileVolumeTargetParams] = Field(default=None, alias="elastifileTargetParams")
    flashblade_target_params: Optional[RecoverOtherNasToFlashbladeVolumeTargetParams] = Field(default=None, alias="flashbladeTargetParams")
    generic_nas_target_params: Optional[RecoverOtherNasToGenericNasVolumeTargetParams] = Field(default=None, alias="genericNasTargetParams")
    gpfs_target_params: Optional[RecoverGpfsToGpfsVolumeTargetParams] = Field(default=None, alias="gpfsTargetParams")
    isilon_target_params: Optional[RecoverOtherNasToIsilonVolumeTargetParams] = Field(default=None, alias="isilonTargetParams")
    netapp_target_params: Optional[RecoverOtherNasToNetappVolumeTargetParams] = Field(default=None, alias="netappTargetParams")
    target_environment: StrictStr = Field(description="Specifies the environment of the recovery target. The corresponding params below must be filled out.", alias="targetEnvironment")
    view_target_params: Optional[RecoverNasVolumeToViewParams] = Field(default=None, alias="viewTargetParams")
    __properties: ClassVar[List[str]] = ["elastifileTargetParams", "flashbladeTargetParams", "genericNasTargetParams", "gpfsTargetParams", "isilonTargetParams", "netappTargetParams", "targetEnvironment", "viewTargetParams"]

    @field_validator('target_environment')
    def target_environment_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['kElastifile', 'kFlashBlade', 'kGenericNas', 'kGPFS', 'kIsilon', 'kNetapp', 'kView']):
            raise ValueError("must be one of enum values ('kElastifile', 'kFlashBlade', 'kGenericNas', 'kGPFS', 'kIsilon', 'kNetapp', 'kView')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RecoverGpfsNasVolumeParams from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of elastifile_target_params
        if self.elastifile_target_params:
            _dict['elastifileTargetParams'] = self.elastifile_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flashblade_target_params
        if self.flashblade_target_params:
            _dict['flashbladeTargetParams'] = self.flashblade_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of generic_nas_target_params
        if self.generic_nas_target_params:
            _dict['genericNasTargetParams'] = self.generic_nas_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpfs_target_params
        if self.gpfs_target_params:
            _dict['gpfsTargetParams'] = self.gpfs_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of isilon_target_params
        if self.isilon_target_params:
            _dict['isilonTargetParams'] = self.isilon_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of netapp_target_params
        if self.netapp_target_params:
            _dict['netappTargetParams'] = self.netapp_target_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of view_target_params
        if self.view_target_params:
            _dict['viewTargetParams'] = self.view_target_params.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverGpfsNasVolumeParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "elastifileTargetParams": RecoverOtherNasToElastifileVolumeTargetParams.from_dict(obj["elastifileTargetParams"]) if obj.get("elastifileTargetParams") is not None else None,
            "flashbladeTargetParams": RecoverOtherNasToFlashbladeVolumeTargetParams.from_dict(obj["flashbladeTargetParams"]) if obj.get("flashbladeTargetParams") is not None else None,
            "genericNasTargetParams": RecoverOtherNasToGenericNasVolumeTargetParams.from_dict(obj["genericNasTargetParams"]) if obj.get("genericNasTargetParams") is not None else None,
            "gpfsTargetParams": RecoverGpfsToGpfsVolumeTargetParams.from_dict(obj["gpfsTargetParams"]) if obj.get("gpfsTargetParams") is not None else None,
            "isilonTargetParams": RecoverOtherNasToIsilonVolumeTargetParams.from_dict(obj["isilonTargetParams"]) if obj.get("isilonTargetParams") is not None else None,
            "netappTargetParams": RecoverOtherNasToNetappVolumeTargetParams.from_dict(obj["netappTargetParams"]) if obj.get("netappTargetParams") is not None else None,
            "targetEnvironment": obj.get("targetEnvironment"),
            "viewTargetParams": RecoverNasVolumeToViewParams.from_dict(obj["viewTargetParams"]) if obj.get("viewTargetParams") is not None else None
        })
        return _obj


