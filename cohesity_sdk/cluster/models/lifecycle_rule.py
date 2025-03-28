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
from cohesity_sdk.cluster.models.abort_incomplete_multipart_upload_action import AbortIncompleteMultipartUploadAction
from cohesity_sdk.cluster.models.expiration_action import ExpirationAction
from cohesity_sdk.cluster.models.lifecycle_rule_filter import LifecycleRuleFilter
from cohesity_sdk.cluster.models.non_current_version_expiration_action import NonCurrentVersionExpirationAction
from typing import Set
from typing_extensions import Self

class LifecycleRule(BaseModel):
    """
    Specifies the Lifecycle configuration rule.
    """ # noqa: E501
    abort_incomplete_multipart_upload_action: Optional[AbortIncompleteMultipartUploadAction] = Field(default=None, alias="abortIncompleteMultipartUploadAction")
    expiration: Optional[ExpirationAction] = None
    filter: Optional[LifecycleRuleFilter] = None
    id: Optional[StrictStr] = Field(description="Specifies the Unique identifier for the rule. The value cannot be longer than 255 characters.")
    non_current_version_expiration_action: Optional[NonCurrentVersionExpirationAction] = Field(default=None, alias="nonCurrentVersionExpirationAction")
    prefix: Optional[StrictStr] = Field(default=None, description="Specifies the prefix used to identify objects that a lifecycle rule applies to.")
    status: Optional[StrictBool] = Field(description="Specifies if the rule is currently being applied.")
    __properties: ClassVar[List[str]] = ["abortIncompleteMultipartUploadAction", "expiration", "filter", "id", "nonCurrentVersionExpirationAction", "prefix", "status"]

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
        """Create an instance of LifecycleRule from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of abort_incomplete_multipart_upload_action
        if self.abort_incomplete_multipart_upload_action:
            _dict['abortIncompleteMultipartUploadAction'] = self.abort_incomplete_multipart_upload_action.to_dict()
        # override the default output from pydantic by calling `to_dict()` of expiration
        if self.expiration:
            _dict['expiration'] = self.expiration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of non_current_version_expiration_action
        if self.non_current_version_expiration_action:
            _dict['nonCurrentVersionExpirationAction'] = self.non_current_version_expiration_action.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if prefix (nullable) is None
        # and model_fields_set contains the field
        if self.prefix is None and "prefix" in self.model_fields_set:
            _dict['prefix'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LifecycleRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "abortIncompleteMultipartUploadAction": AbortIncompleteMultipartUploadAction.from_dict(obj["abortIncompleteMultipartUploadAction"]) if obj.get("abortIncompleteMultipartUploadAction") is not None else None,
            "expiration": ExpirationAction.from_dict(obj["expiration"]) if obj.get("expiration") is not None else None,
            "filter": LifecycleRuleFilter.from_dict(obj["filter"]) if obj.get("filter") is not None else None,
            "id": obj.get("id"),
            "nonCurrentVersionExpirationAction": NonCurrentVersionExpirationAction.from_dict(obj["nonCurrentVersionExpirationAction"]) if obj.get("nonCurrentVersionExpirationAction") is not None else None,
            "prefix": obj.get("prefix"),
            "status": obj.get("status")
        })
        return _obj


