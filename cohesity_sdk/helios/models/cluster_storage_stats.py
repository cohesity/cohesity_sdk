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
from typing import Set
from typing_extensions import Self

class ClusterStorageStats(BaseModel):
    """
    Specifies the Cluster storage stats.
    """ # noqa: E501
    data_protection_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical size of protected objects in bytes.", alias="dataProtectionLogicalUsageBytes")
    data_protection_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the physical size of protected objects in bytes.", alias="dataProtectionPhysicalUsageBytes")
    file_services_logical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logical size consumed by file services in bytes.", alias="fileServicesLogicalUsageBytes")
    file_services_physical_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the physical size consumed by file services in bytes.", alias="fileServicesPhysicalUsageBytes")
    local_available_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the local storage currently available on the cluster in bytes.", alias="localAvailableBytes")
    local_usage_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the local storage currently in use on the cluster in bytes.", alias="localUsageBytes")
    total_capacity_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the total capacity of the cluster in bytes.", alias="totalCapacityBytes")
    __properties: ClassVar[List[str]] = ["dataProtectionLogicalUsageBytes", "dataProtectionPhysicalUsageBytes", "fileServicesLogicalUsageBytes", "fileServicesPhysicalUsageBytes", "localAvailableBytes", "localUsageBytes", "totalCapacityBytes"]

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
        """Create an instance of ClusterStorageStats from a JSON string"""
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
        # set to None if data_protection_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_protection_logical_usage_bytes is None and "data_protection_logical_usage_bytes" in self.model_fields_set:
            _dict['dataProtectionLogicalUsageBytes'] = None

        # set to None if data_protection_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.data_protection_physical_usage_bytes is None and "data_protection_physical_usage_bytes" in self.model_fields_set:
            _dict['dataProtectionPhysicalUsageBytes'] = None

        # set to None if file_services_logical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_logical_usage_bytes is None and "file_services_logical_usage_bytes" in self.model_fields_set:
            _dict['fileServicesLogicalUsageBytes'] = None

        # set to None if file_services_physical_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.file_services_physical_usage_bytes is None and "file_services_physical_usage_bytes" in self.model_fields_set:
            _dict['fileServicesPhysicalUsageBytes'] = None

        # set to None if local_available_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_available_bytes is None and "local_available_bytes" in self.model_fields_set:
            _dict['localAvailableBytes'] = None

        # set to None if local_usage_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.local_usage_bytes is None and "local_usage_bytes" in self.model_fields_set:
            _dict['localUsageBytes'] = None

        # set to None if total_capacity_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.total_capacity_bytes is None and "total_capacity_bytes" in self.model_fields_set:
            _dict['totalCapacityBytes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterStorageStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataProtectionLogicalUsageBytes": obj.get("dataProtectionLogicalUsageBytes"),
            "dataProtectionPhysicalUsageBytes": obj.get("dataProtectionPhysicalUsageBytes"),
            "fileServicesLogicalUsageBytes": obj.get("fileServicesLogicalUsageBytes"),
            "fileServicesPhysicalUsageBytes": obj.get("fileServicesPhysicalUsageBytes"),
            "localAvailableBytes": obj.get("localAvailableBytes"),
            "localUsageBytes": obj.get("localUsageBytes"),
            "totalCapacityBytes": obj.get("totalCapacityBytes")
        })
        return _obj


