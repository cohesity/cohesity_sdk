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
from cohesity_sdk.helios.models.backup_generic_stats import BackupGenericStats
from cohesity_sdk.helios.models.backup_nas_stats import BackupNasStats
from cohesity_sdk.helios.models.object_string_identifier import ObjectStringIdentifier
from cohesity_sdk.helios.models.stats_task_info import StatsTaskInfo
from typing import Optional, Set
from typing_extensions import Self

class ObjectStatsInfo(BaseModel):
    """
    Specifies the Stats of an object.
    """ # noqa: E501
    entity_id: Optional[ObjectStringIdentifier] = Field(default=None, alias="entityId")
    environment: Optional[StrictStr] = Field(default=None, description="Specifies the environment of the object.")
    id: Optional[StrictInt] = Field(default=None, description="Specifies object id.")
    name: Optional[StrictStr] = Field(default=None, description="Specifies the name of the object.")
    source_id: Optional[StrictInt] = Field(default=None, description="Specifies registered source id to which object belongs.", alias="sourceId")
    source_name: Optional[StrictStr] = Field(default=None, description="Specifies registered source name to which object belongs.", alias="sourceName")
    backup_generic_stats: Optional[BackupGenericStats] = Field(default=None, alias="backupGenericStats")
    nas_stats: Optional[BackupNasStats] = Field(default=None, alias="nasStats")
    failed_attempts: Optional[List[StatsTaskInfo]] = Field(default=None, description="Specifies stats for failed attempts of this object.", alias="failedAttempts")
    __properties: ClassVar[List[str]] = ["entityId", "environment", "id", "name", "sourceId", "sourceName", "backupGenericStats", "nasStats", "failedAttempts"]

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
        """Create an instance of ObjectStatsInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of entity_id
        if self.entity_id:
            _dict['entityId'] = self.entity_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backup_generic_stats
        if self.backup_generic_stats:
            _dict['backupGenericStats'] = self.backup_generic_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of nas_stats
        if self.nas_stats:
            _dict['nasStats'] = self.nas_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in failed_attempts (list)
        _items = []
        if self.failed_attempts:
            for _item_failed_attempts in self.failed_attempts:
                if _item_failed_attempts:
                    _items.append(_item_failed_attempts.to_dict())
            _dict['failedAttempts'] = _items
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

        # set to None if source_id (nullable) is None
        # and model_fields_set contains the field
        if self.source_id is None and "source_id" in self.model_fields_set:
            _dict['sourceId'] = None

        # set to None if source_name (nullable) is None
        # and model_fields_set contains the field
        if self.source_name is None and "source_name" in self.model_fields_set:
            _dict['sourceName'] = None

        # set to None if failed_attempts (nullable) is None
        # and model_fields_set contains the field
        if self.failed_attempts is None and "failed_attempts" in self.model_fields_set:
            _dict['failedAttempts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ObjectStatsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entityId": ObjectStringIdentifier.from_dict(obj["entityId"]) if obj.get("entityId") is not None else None,
            "environment": obj.get("environment"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "sourceId": obj.get("sourceId"),
            "sourceName": obj.get("sourceName"),
            "backupGenericStats": BackupGenericStats.from_dict(obj["backupGenericStats"]) if obj.get("backupGenericStats") is not None else None,
            "nasStats": BackupNasStats.from_dict(obj["nasStats"]) if obj.get("nasStats") is not None else None,
            "failedAttempts": [StatsTaskInfo.from_dict(_item) for _item in obj["failedAttempts"]] if obj.get("failedAttempts") is not None else None
        })
        return _obj


