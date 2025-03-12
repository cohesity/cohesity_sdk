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
from cohesity_sdk.helios.models.full_backup_policy import FullBackupPolicy
from cohesity_sdk.helios.models.full_schedule_and_retention import FullScheduleAndRetention
from cohesity_sdk.helios.models.incremental_backup_policy import IncrementalBackupPolicy
from cohesity_sdk.helios.models.primary_backup_target import PrimaryBackupTarget
from cohesity_sdk.helios.models.retention import Retention
from typing import Set
from typing_extensions import Self

class RegularBackupPolicy(BaseModel):
    """
    Specifies the Incremental and Full policy settings and also the common Retention policy settings.\"
    """ # noqa: E501
    full: Optional[FullBackupPolicy] = None
    full_backups: Optional[List[FullScheduleAndRetention]] = Field(default=None, description="Specifies multiple schedules and retentions for full backup. Specify either of the 'full' or 'fullBackups' values. Its recommended to use 'fullBaackups' value since 'full' will be deprecated after few releases.", alias="fullBackups")
    incremental: Optional[IncrementalBackupPolicy] = None
    primary_backup_target: Optional[PrimaryBackupTarget] = Field(default=None, alias="primaryBackupTarget")
    retention: Optional[Retention] = None
    __properties: ClassVar[List[str]] = ["full", "fullBackups", "incremental", "primaryBackupTarget", "retention"]

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
        """Create an instance of RegularBackupPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of full
        if self.full:
            _dict['full'] = self.full.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in full_backups (list)
        _items = []
        if self.full_backups:
            for _item_full_backups in self.full_backups:
                if _item_full_backups:
                    _items.append(_item_full_backups.to_dict())
            _dict['fullBackups'] = _items
        # override the default output from pydantic by calling `to_dict()` of incremental
        if self.incremental:
            _dict['incremental'] = self.incremental.to_dict()
        # override the default output from pydantic by calling `to_dict()` of primary_backup_target
        if self.primary_backup_target:
            _dict['primaryBackupTarget'] = self.primary_backup_target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retention
        if self.retention:
            _dict['retention'] = self.retention.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegularBackupPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "full": FullBackupPolicy.from_dict(obj["full"]) if obj.get("full") is not None else None,
            "fullBackups": [FullScheduleAndRetention.from_dict(_item) for _item in obj["fullBackups"]] if obj.get("fullBackups") is not None else None,
            "incremental": IncrementalBackupPolicy.from_dict(obj["incremental"]) if obj.get("incremental") is not None else None,
            "primaryBackupTarget": PrimaryBackupTarget.from_dict(obj["primaryBackupTarget"]) if obj.get("primaryBackupTarget") is not None else None,
            "retention": Retention.from_dict(obj["retention"]) if obj.get("retention") is not None else None
        })
        return _obj


