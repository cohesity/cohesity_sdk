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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.aws_recover_s3_new_target_config import AwsRecoverS3NewTargetConfig
from typing import Optional, Set
from typing_extensions import Self

class AwsTargetParamsForRecoverS3(BaseModel):
    """
    Specifies the parameters for an AWS recovery target.
    """ # noqa: E501
    continue_on_error: Optional[StrictBool] = Field(default=None, description="Specifies whether to continue restore on receiving error or not. Default is true.", alias="continueOnError")
    new_target_config: Optional[AwsRecoverS3NewTargetConfig] = Field(default=None, alias="newTargetConfig")
    object_prefix: Optional[StrictStr] = Field(default=None, description="Specifies the prefix to be added to all the objects being recovered.", alias="objectPrefix")
    overwrite_existing: Optional[StrictBool] = Field(default=None, description="Specifies whether to override the existing objects. Default is false.", alias="overwriteExisting")
    preserve_attributes: Optional[StrictBool] = Field(default=None, description="Specifies whether to preserve the objects attributes at the time of restore. Default is true.", alias="preserveAttributes")
    recover_to_original_target: Optional[StrictBool] = Field(description="Specifies whether to recover to the original target. If true, originalTargetConfig must be specified. If false, newTargetConfig must be specified.", alias="recoverToOriginalTarget")
    __properties: ClassVar[List[str]] = ["continueOnError", "newTargetConfig", "objectPrefix", "overwriteExisting", "preserveAttributes", "recoverToOriginalTarget"]

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
        """Create an instance of AwsTargetParamsForRecoverS3 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of new_target_config
        if self.new_target_config:
            _dict['newTargetConfig'] = self.new_target_config.to_dict()
        # set to None if continue_on_error (nullable) is None
        # and model_fields_set contains the field
        if self.continue_on_error is None and "continue_on_error" in self.model_fields_set:
            _dict['continueOnError'] = None

        # set to None if object_prefix (nullable) is None
        # and model_fields_set contains the field
        if self.object_prefix is None and "object_prefix" in self.model_fields_set:
            _dict['objectPrefix'] = None

        # set to None if overwrite_existing (nullable) is None
        # and model_fields_set contains the field
        if self.overwrite_existing is None and "overwrite_existing" in self.model_fields_set:
            _dict['overwriteExisting'] = None

        # set to None if preserve_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.preserve_attributes is None and "preserve_attributes" in self.model_fields_set:
            _dict['preserveAttributes'] = None

        # set to None if recover_to_original_target (nullable) is None
        # and model_fields_set contains the field
        if self.recover_to_original_target is None and "recover_to_original_target" in self.model_fields_set:
            _dict['recoverToOriginalTarget'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsTargetParamsForRecoverS3 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "continueOnError": obj.get("continueOnError"),
            "newTargetConfig": AwsRecoverS3NewTargetConfig.from_dict(obj["newTargetConfig"]) if obj.get("newTargetConfig") is not None else None,
            "objectPrefix": obj.get("objectPrefix"),
            "overwriteExisting": obj.get("overwriteExisting"),
            "preserveAttributes": obj.get("preserveAttributes"),
            "recoverToOriginalTarget": obj.get("recoverToOriginalTarget")
        })
        return _obj


