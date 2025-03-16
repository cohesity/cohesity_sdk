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
from typing import Optional, Set
from typing_extensions import Self

class QuotaPolicy(BaseModel):
    """
    Specifies a quota limit that can be optionally applied to Views and Storage Domains. At the View level, this quota defines a logical limit for usage on the View. At the Storage Domain level, this quota defines a physical limit or a default logical View limit. If a physical quota is specified for Storage Domain, this quota defines a physical limit for the usage on the Storage Domain. If a default logical View quota is specified for Storage Domain, this limit is inherited by all the Views in that Storage Domain. However, this inherited quota can be overwritten at the View level. A new write is not allowed if the resource will exceed the specified quota. However, it takes time for the Cohesity Cluster to calculate the usage across Nodes, so the limit may be exceeded by a small amount. In addition, if the limit is increased or data is removed, there may be a delay before the Cohesity Cluster allows more data to be written to the resource, as the Cluster calculates the usage across Nodes.
    """ # noqa: E501
    alert_limit_bytes: Optional[StrictInt] = Field(default=None, description="Specifies if an alert should be triggered when the usage of this resource exceeds this quota limit. This limit is optional and is specified in bytes. If no value is specified, there is no limit.", alias="alertLimitBytes")
    alert_threshold_percentage: Optional[StrictInt] = Field(default=None, description="Supported only for user quota policy. Specifies when the usage goes above an alert threshold percentage which is: HardLimitBytes * AlertThresholdPercentage, eg: 80% of HardLimitBytes Can only be set if HardLimitBytes is set. Cannot be set if AlertLimitBytes is already set.", alias="alertThresholdPercentage")
    hard_limit_bytes: Optional[StrictInt] = Field(default=None, description="Specifies an optional quota limit on the usage allowed for this resource. This limit is specified in bytes. If no value is specified, there is no limit.", alias="hardLimitBytes")
    __properties: ClassVar[List[str]] = ["alertLimitBytes", "alertThresholdPercentage", "hardLimitBytes"]

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
        """Create an instance of QuotaPolicy from a JSON string"""
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
        # set to None if alert_limit_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.alert_limit_bytes is None and "alert_limit_bytes" in self.model_fields_set:
            _dict['alertLimitBytes'] = None

        # set to None if alert_threshold_percentage (nullable) is None
        # and model_fields_set contains the field
        if self.alert_threshold_percentage is None and "alert_threshold_percentage" in self.model_fields_set:
            _dict['alertThresholdPercentage'] = None

        # set to None if hard_limit_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.hard_limit_bytes is None and "hard_limit_bytes" in self.model_fields_set:
            _dict['hardLimitBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuotaPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertLimitBytes": obj.get("alertLimitBytes"),
            "alertThresholdPercentage": obj.get("alertThresholdPercentage"),
            "hardLimitBytes": obj.get("hardLimitBytes")
        })
        return _obj


