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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.recover_pure_san_volume_new_source_config import RecoverPureSanVolumeNewSourceConfig
from cohesity_sdk.cluster.models.recover_pure_san_volume_original_source_config import RecoverPureSanVolumeOriginalSourceConfig
from typing import Optional, Set
from typing_extensions import Self

class RecoverPureVolumeTargetParams(BaseModel):
    """
    Specifies the target object parameters to recover the Pure San Volume.
    """ # noqa: E501
    new_source_config: Optional[RecoverPureSanVolumeNewSourceConfig] = Field(default=None, alias="newSourceConfig")
    original_source_config: Optional[RecoverPureSanVolumeOriginalSourceConfig] = Field(default=None, alias="originalSourceConfig")
    recover_to_new_source: StrictBool = Field(description="Specifies whether to recover to a new source.", alias="recoverToNewSource")
    use_thin_clone: Optional[StrictBool] = Field(default=None, description="Specifies whether to use thin clone to restore storage array snapshots.", alias="useThinClone")
    __properties: ClassVar[List[str]] = ["newSourceConfig", "originalSourceConfig", "recoverToNewSource", "useThinClone"]

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
        """Create an instance of RecoverPureVolumeTargetParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of new_source_config
        if self.new_source_config:
            _dict['newSourceConfig'] = self.new_source_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of original_source_config
        if self.original_source_config:
            _dict['originalSourceConfig'] = self.original_source_config.to_dict()
        # set to None if use_thin_clone (nullable) is None
        # and model_fields_set contains the field
        if self.use_thin_clone is None and "use_thin_clone" in self.model_fields_set:
            _dict['useThinClone'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverPureVolumeTargetParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "newSourceConfig": RecoverPureSanVolumeNewSourceConfig.from_dict(obj["newSourceConfig"]) if obj.get("newSourceConfig") is not None else None,
            "originalSourceConfig": RecoverPureSanVolumeOriginalSourceConfig.from_dict(obj["originalSourceConfig"]) if obj.get("originalSourceConfig") is not None else None,
            "recoverToNewSource": obj.get("recoverToNewSource"),
            "useThinClone": obj.get("useThinClone")
        })
        return _obj


