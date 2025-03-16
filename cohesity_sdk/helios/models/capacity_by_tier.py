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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class CapacityByTier(BaseModel):
    """
    CapacityByTier provides the physical capacity in bytes of each storage tier.
    """ # noqa: E501
    max_physical_capacity_bytes_tier: Optional[StrictInt] = Field(default=None, description="maxPhysicalCapacityBytesTier is the maximum physical capacity in bytes of the storage tier.", alias="maxPhysicalCapacityBytesTier")
    storage_tier: Optional[StrictStr] = Field(default=None, description="StorageTier is the type of StorageTier. StorageTierType represents the various values for the Storage Tier. 'kPCIeSSD' indicates storage tier type of Pci Solid State Drive. 'kSATAHDD' indicates storage tier type of SATA Solid State Drive. 'kSATAHDD' indicates storage tier type of SATA Hard Disk Drive. 'kCLOUD' indicates storage tier type of Cloud.", alias="storageTier")
    __properties: ClassVar[List[str]] = ["maxPhysicalCapacityBytesTier", "storageTier"]

    @field_validator('storage_tier')
    def storage_tier_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['PCIeSSD', 'SATASSD', 'SATAHDD', 'CLOUD', 'INVALID']):
            raise ValueError("must be one of enum values ('PCIeSSD', 'SATASSD', 'SATAHDD', 'CLOUD', 'INVALID')")
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
        """Create an instance of CapacityByTier from a JSON string"""
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
        # set to None if max_physical_capacity_bytes_tier (nullable) is None
        # and model_fields_set contains the field
        if self.max_physical_capacity_bytes_tier is None and "max_physical_capacity_bytes_tier" in self.model_fields_set:
            _dict['maxPhysicalCapacityBytesTier'] = None

        # set to None if storage_tier (nullable) is None
        # and model_fields_set contains the field
        if self.storage_tier is None and "storage_tier" in self.model_fields_set:
            _dict['storageTier'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CapacityByTier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maxPhysicalCapacityBytesTier": obj.get("maxPhysicalCapacityBytesTier"),
            "storageTier": obj.get("storageTier")
        })
        return _obj


