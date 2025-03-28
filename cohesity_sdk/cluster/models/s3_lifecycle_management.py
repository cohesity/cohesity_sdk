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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.cluster.models.lifecycle_rule import LifecycleRule
from typing import Set
from typing_extensions import Self

class S3LifecycleManagement(BaseModel):
    """
    Specifies the S3 Lifecycle policy of the bucket. If not specified no Lifecycle management is performed for objects in this bucket.
    """ # noqa: E501
    rules: Optional[List[LifecycleRule]] = Field(default=None, description="Specifies Lifecycle configuration rules for an Amazon S3 bucket. A maximum of 1000 rules can be specified.")
    version_id: Optional[StrictInt] = Field(default=None, description="Specifies a unique monotonically increasing version for the lifecycle configuration.", alias="versionId")
    __properties: ClassVar[List[str]] = ["rules", "versionId"]

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
        """Create an instance of S3LifecycleManagement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item_rules in self.rules:
                if _item_rules:
                    _items.append(_item_rules.to_dict())
            _dict['rules'] = _items
        # set to None if rules (nullable) is None
        # and model_fields_set contains the field
        if self.rules is None and "rules" in self.model_fields_set:
            _dict['rules'] = None

        # set to None if version_id (nullable) is None
        # and model_fields_set contains the field
        if self.version_id is None and "version_id" in self.model_fields_set:
            _dict['versionId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of S3LifecycleManagement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rules": [LifecycleRule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "versionId": obj.get("versionId")
        })
        return _obj


