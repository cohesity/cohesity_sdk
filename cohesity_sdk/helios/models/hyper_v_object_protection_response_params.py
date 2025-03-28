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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.indexing_policy import IndexingPolicy
from typing import Set
from typing_extensions import Self

class HyperVObjectProtectionResponseParams(BaseModel):
    """
    Specifies the parameters which are specific to HyperV object protection.
    """ # noqa: E501
    backups_copy_only: Optional[StrictBool] = Field(default=None, description="Specifies whether the backups should be copy-only.", alias="backupsCopyOnly")
    exclude_object_ids: Optional[List[Optional[StrictInt]]] = Field(default=None, description="Specifies the list of IDs of the objects to not be protected by this Protection Group. This can be used to ignore specific objects under a parent object which has been included for protection.", alias="excludeObjectIds")
    app_consistent_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent.", alias="appConsistentSnapshot")
    fallback_to_crash_consistent_snapshot: Optional[StrictBool] = Field(default=None, description="Specifies whether or not to fallback to a crash consistent snapshot in the event that an app consistent snapshot fails.", alias="fallbackToCrashConsistentSnapshot")
    indexing_policy: Optional[IndexingPolicy] = Field(default=None, alias="indexingPolicy")
    __properties: ClassVar[List[str]] = ["backupsCopyOnly", "excludeObjectIds", "appConsistentSnapshot", "fallbackToCrashConsistentSnapshot", "indexingPolicy"]

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
        """Create an instance of HyperVObjectProtectionResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of indexing_policy
        if self.indexing_policy:
            _dict['indexingPolicy'] = self.indexing_policy.to_dict()
        # set to None if backups_copy_only (nullable) is None
        # and model_fields_set contains the field
        if self.backups_copy_only is None and "backups_copy_only" in self.model_fields_set:
            _dict['backupsCopyOnly'] = None

        # set to None if app_consistent_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.app_consistent_snapshot is None and "app_consistent_snapshot" in self.model_fields_set:
            _dict['appConsistentSnapshot'] = None

        # set to None if fallback_to_crash_consistent_snapshot (nullable) is None
        # and model_fields_set contains the field
        if self.fallback_to_crash_consistent_snapshot is None and "fallback_to_crash_consistent_snapshot" in self.model_fields_set:
            _dict['fallbackToCrashConsistentSnapshot'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HyperVObjectProtectionResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backupsCopyOnly": obj.get("backupsCopyOnly"),
            "excludeObjectIds": obj.get("excludeObjectIds"),
            "appConsistentSnapshot": obj.get("appConsistentSnapshot"),
            "fallbackToCrashConsistentSnapshot": obj.get("fallbackToCrashConsistentSnapshot"),
            "indexingPolicy": IndexingPolicy.from_dict(obj["indexingPolicy"]) if obj.get("indexingPolicy") is not None else None
        })
        return _obj


