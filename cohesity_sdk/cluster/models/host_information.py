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
from typing import Set
from typing_extensions import Self

class HostInformation(BaseModel):
    """
    Specifies the host information for a objects. This is mainly populated in case of App objects where app object is hosted by another object such as VM or physical server.
    """ # noqa: E501
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the object.")
    id: Optional[StrictStr] = Field(default=None, description="Specifies the id of the host object.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the host object.")
    __properties: ClassVar[List[str]] = ["environment", "id", "name"]

    @field_validator('environment')
    def environment_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
            raise ValueError("must be one of enum values ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
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
        """Create an instance of HostInformation from a JSON string"""
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
        # set to None if environment (nullable) is None
        # and model_fields_set contains the field
        if self.environment is None and "environment" in self.model_fields_set:
            _dict['environment'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HostInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name")
        })
        return _obj


