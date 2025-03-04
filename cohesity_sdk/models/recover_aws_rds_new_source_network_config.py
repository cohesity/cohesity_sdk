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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.models.recovery_object_identifier import RecoveryObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class RecoverAwsRdsNewSourceNetworkConfig(BaseModel):
    """
    Specifies the network config parameters to be applied for AWS RDS if recovering to new Source.
    """ # noqa: E501
    availability_zone: Optional[RecoveryObjectIdentifier] = Field(default=None, alias="availabilityZone")
    security_groups: Optional[List[RecoveryObjectIdentifier]] = Field(default=None, description="Specifies the network security groups within above VPC.", alias="securityGroups")
    subnet: RecoveryObjectIdentifier
    vpc: RecoveryObjectIdentifier
    __properties: ClassVar[List[str]] = ["availabilityZone", "securityGroups", "subnet", "vpc"]

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
        """Create an instance of RecoverAwsRdsNewSourceNetworkConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of availability_zone
        if self.availability_zone:
            _dict['availabilityZone'] = self.availability_zone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in security_groups (list)
        _items = []
        if self.security_groups:
            for _item_security_groups in self.security_groups:
                if _item_security_groups:
                    _items.append(_item_security_groups.to_dict())
            _dict['securityGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of subnet
        if self.subnet:
            _dict['subnet'] = self.subnet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpc
        if self.vpc:
            _dict['vpc'] = self.vpc.to_dict()
        # set to None if security_groups (nullable) is None
        # and model_fields_set contains the field
        if self.security_groups is None and "security_groups" in self.model_fields_set:
            _dict['securityGroups'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RecoverAwsRdsNewSourceNetworkConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availabilityZone": RecoveryObjectIdentifier.from_dict(obj["availabilityZone"]) if obj.get("availabilityZone") is not None else None,
            "securityGroups": [RecoveryObjectIdentifier.from_dict(_item) for _item in obj["securityGroups"]] if obj.get("securityGroups") is not None else None,
            "subnet": RecoveryObjectIdentifier.from_dict(obj["subnet"]) if obj.get("subnet") is not None else None,
            "vpc": RecoveryObjectIdentifier.from_dict(obj["vpc"]) if obj.get("vpc") is not None else None
        })
        return _obj


