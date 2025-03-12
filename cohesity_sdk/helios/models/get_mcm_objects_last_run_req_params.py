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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.activity_stats_params import ActivityStatsParams
from cohesity_sdk.helios.models.archival_run_filter_params import ArchivalRunFilterParams
from cohesity_sdk.helios.models.backup_run_filter_params import BackupRunFilterParams
from cohesity_sdk.helios.models.mcm_object_identifier import McmObjectIdentifier
from typing import Optional, Set
from typing_extensions import Self

class GetMcmObjectsLastRunReqParams(BaseModel):
    """
    Specifies the params to filter object last run activities.
    """ # noqa: E501
    activity_types: Optional[List[StrictStr]] = Field(default=None, description="Specifies the activity types.", alias="activityTypes")
    archival_run_params: Optional[ArchivalRunFilterParams] = Field(default=None, alias="archivalRunParams")
    backup_run_params: Optional[BackupRunFilterParams] = Field(default=None, alias="backupRunParams")
    environments: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of environments.")
    exclude_data: Optional[StrictBool] = Field(default=None, description="Specifies whether to exclude activity information from the response. If not specified or false, activity information will be included.", alias="excludeData")
    exclude_stats: Optional[StrictBool] = Field(default=None, description="Specifies whether to exclude stats information from the response. If not specified or false, stats information will be included.", alias="excludeStats")
    include_details: Optional[StrictBool] = Field(default=None, description="Specifies whether the response should return activity details. If this is true, all activity info will be returned. Otherwise only object id, activity id, status and sla info will be returned. If not specified, default is false.", alias="includeDetails")
    is_protected: Optional[StrictBool] = Field(default=None, description="Specifies whether to return runs for only protected objects. By default it's false.", alias="isProtected")
    is_sla_violated: Optional[StrictBool] = Field(default=None, description="Specifies whether the last run violated sla.", alias="isSlaViolated")
    object_identifiers: Optional[List[McmObjectIdentifier]] = Field(default=None, description="Specifies the list of object identifiers, only last runs for these objects will be returned.", alias="objectIdentifiers")
    source_identifier: Optional[McmObjectIdentifier] = Field(default=None, alias="sourceIdentifier")
    stats_params: Optional[ActivityStatsParams] = Field(default=None, alias="statsParams")
    statuses: Optional[List[StrictStr]] = Field(default=None, description="Specifies the list of statuses to filter activity events.")
    __properties: ClassVar[List[str]] = ["activityTypes", "archivalRunParams", "backupRunParams", "environments", "excludeData", "excludeStats", "includeDetails", "isProtected", "isSlaViolated", "objectIdentifiers", "sourceIdentifier", "statsParams", "statuses"]

    @field_validator('activity_types')
    def activity_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['BackupRun', 'Restore', 'ArchivalRun']):
                raise ValueError("each list item must be one of ('BackupRun', 'Restore', 'ArchivalRun')")
        return value

    @field_validator('environments')
    def environments_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc']):
                raise ValueError("each list item must be one of ('kVMware', 'kHyperV', 'kAzure', 'kKVM', 'kAWS', 'kAzureSQL', 'kAcropolis', 'kGCP', 'kPhysical', 'kPhysicalFiles', 'kIsilon', 'kNetapp', 'kGenericNas', 'kFlashBlade', 'kElastifile', 'kGPFS', 'kPure', 'kIbmFlashSystem', 'kNimble', 'kSQL', 'kOracle', 'kExchange', 'kAD', 'kView', 'kO365', 'kHyperFlex', 'kKubernetes', 'kCassandra', 'kMongoDB', 'kCouchbase', 'kHdfs', 'kHive', 'kHBase', 'kUDA', 'kSfdc')")
        return value

    @field_validator('statuses')
    def statuses_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped']):
                raise ValueError("each list item must be one of ('Accepted', 'Running', 'Canceled', 'Canceling', 'Failed', 'Missed', 'Succeeded', 'SucceededWithWarning', 'OnHold', 'Finalizing', 'Skipped')")
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
        """Create an instance of GetMcmObjectsLastRunReqParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of archival_run_params
        if self.archival_run_params:
            _dict['archivalRunParams'] = self.archival_run_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backup_run_params
        if self.backup_run_params:
            _dict['backupRunParams'] = self.backup_run_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in object_identifiers (list)
        _items = []
        if self.object_identifiers:
            for _item_object_identifiers in self.object_identifiers:
                if _item_object_identifiers:
                    _items.append(_item_object_identifiers.to_dict())
            _dict['objectIdentifiers'] = _items
        # override the default output from pydantic by calling `to_dict()` of source_identifier
        if self.source_identifier:
            _dict['sourceIdentifier'] = self.source_identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stats_params
        if self.stats_params:
            _dict['statsParams'] = self.stats_params.to_dict()
        # set to None if activity_types (nullable) is None
        # and model_fields_set contains the field
        if self.activity_types is None and "activity_types" in self.model_fields_set:
            _dict['activityTypes'] = None

        # set to None if environments (nullable) is None
        # and model_fields_set contains the field
        if self.environments is None and "environments" in self.model_fields_set:
            _dict['environments'] = None

        # set to None if exclude_data (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_data is None and "exclude_data" in self.model_fields_set:
            _dict['excludeData'] = None

        # set to None if exclude_stats (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_stats is None and "exclude_stats" in self.model_fields_set:
            _dict['excludeStats'] = None

        # set to None if include_details (nullable) is None
        # and model_fields_set contains the field
        if self.include_details is None and "include_details" in self.model_fields_set:
            _dict['includeDetails'] = None

        # set to None if is_protected (nullable) is None
        # and model_fields_set contains the field
        if self.is_protected is None and "is_protected" in self.model_fields_set:
            _dict['isProtected'] = None

        # set to None if is_sla_violated (nullable) is None
        # and model_fields_set contains the field
        if self.is_sla_violated is None and "is_sla_violated" in self.model_fields_set:
            _dict['isSlaViolated'] = None

        # set to None if object_identifiers (nullable) is None
        # and model_fields_set contains the field
        if self.object_identifiers is None and "object_identifiers" in self.model_fields_set:
            _dict['objectIdentifiers'] = None

        # set to None if statuses (nullable) is None
        # and model_fields_set contains the field
        if self.statuses is None and "statuses" in self.model_fields_set:
            _dict['statuses'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetMcmObjectsLastRunReqParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activityTypes": obj.get("activityTypes"),
            "archivalRunParams": ArchivalRunFilterParams.from_dict(obj["archivalRunParams"]) if obj.get("archivalRunParams") is not None else None,
            "backupRunParams": BackupRunFilterParams.from_dict(obj["backupRunParams"]) if obj.get("backupRunParams") is not None else None,
            "environments": obj.get("environments"),
            "excludeData": obj.get("excludeData"),
            "excludeStats": obj.get("excludeStats"),
            "includeDetails": obj.get("includeDetails"),
            "isProtected": obj.get("isProtected"),
            "isSlaViolated": obj.get("isSlaViolated"),
            "objectIdentifiers": [McmObjectIdentifier.from_dict(_item) for _item in obj["objectIdentifiers"]] if obj.get("objectIdentifiers") is not None else None,
            "sourceIdentifier": McmObjectIdentifier.from_dict(obj["sourceIdentifier"]) if obj.get("sourceIdentifier") is not None else None,
            "statsParams": ActivityStatsParams.from_dict(obj["statsParams"]) if obj.get("statsParams") is not None else None,
            "statuses": obj.get("statuses")
        })
        return _obj


