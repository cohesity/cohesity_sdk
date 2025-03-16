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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.aws_object_level_params import AwsObjectLevelParams
from cohesity_sdk.cluster.models.ebs_volume_exclusion_params import EbsVolumeExclusionParams
from typing import Optional, Set
from typing_extensions import Self

class AwsSnapshotManagerObjectProtectionParams(BaseModel):
    """
    Specifies the parameters which are specific to AWS Object Protection using AWS native snapshot orchestration with snapshot manager. Atlease one of tags or objects must be specified.
    """ # noqa: E501
    ami_creation_frequency: Optional[StrictInt] = Field(default=None, description="The frequency of AMI creation. This should be set if the option to create AMI is set. A value of n creates an AMI from the snapshots after every n runs. eg. n = 2 implies every alternate backup run starting from the first will create an AMI.", alias="amiCreationFrequency")
    create_ami: Optional[StrictBool] = Field(default=None, description="Specifies whether AMI should be created after taking snapshots of the instance.", alias="createAmi")
    objects: Optional[List[AwsObjectLevelParams]] = Field(default=None, description="Specifies the objects to be protected.")
    volume_exclusion_params: Optional[EbsVolumeExclusionParams] = Field(default=None, alias="volumeExclusionParams")
    __properties: ClassVar[List[str]] = ["amiCreationFrequency", "createAmi", "objects", "volumeExclusionParams"]

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
        """Create an instance of AwsSnapshotManagerObjectProtectionParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # override the default output from pydantic by calling `to_dict()` of volume_exclusion_params
        if self.volume_exclusion_params:
            _dict['volumeExclusionParams'] = self.volume_exclusion_params.to_dict()
        # set to None if ami_creation_frequency (nullable) is None
        # and model_fields_set contains the field
        if self.ami_creation_frequency is None and "ami_creation_frequency" in self.model_fields_set:
            _dict['amiCreationFrequency'] = None

        # set to None if create_ami (nullable) is None
        # and model_fields_set contains the field
        if self.create_ami is None and "create_ami" in self.model_fields_set:
            _dict['createAmi'] = None

        # set to None if volume_exclusion_params (nullable) is None
        # and model_fields_set contains the field
        if self.volume_exclusion_params is None and "volume_exclusion_params" in self.model_fields_set:
            _dict['volumeExclusionParams'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsSnapshotManagerObjectProtectionParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amiCreationFrequency": obj.get("amiCreationFrequency"),
            "createAmi": obj.get("createAmi"),
            "objects": [AwsObjectLevelParams.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "volumeExclusionParams": EbsVolumeExclusionParams.from_dict(obj["volumeExclusionParams"]) if obj.get("volumeExclusionParams") is not None else None
        })
        return _obj


