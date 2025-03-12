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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.failover_object import FailoverObject
from typing import Optional, Set
from typing_extensions import Self

class FailoverRunConfiguration(BaseModel):
    """
    Specifies the configuration required for execting special run as a part of failover workflow. This special run is triggered during palnned failover to sync the source cluster to replication cluster with minimum possible delta. Please note that if this object is passed then this special run will ignore the other archivals and retention settings.
    """ # noqa: E501
    cancel_non_failover_runs: Optional[StrictBool] = Field(default=None, description="If set to true, other ongoing runs backing up the same set of entities being failed over will be initiated for cancellation. Non conflicting run operations such as replications to other clusters, archivals will not be cancelled. If set to false, then new run will wait for all the pending operations to finish normally before scheduling a new backup/replication.", alias="cancelNonFailoverRuns")
    objects: Optional[List[FailoverObject]] = Field(description="Specifies the list of all local entity ids of all the objects being failed from the source cluster.")
    pause_next_runs: Optional[StrictBool] = Field(default=None, description="If this is set to true then unless failover operation is completed, all the next runs will be pasued.", alias="pauseNextRuns")
    protection_group_id: Optional[StrictStr] = Field(default=None, description="Specifies the active protection group id on the source cluster from where the objects are being failed over.", alias="protectionGroupId")
    replication_cluster_id: Optional[StrictInt] = Field(description="Specifies the replication cluster Id where planned run will replicate objects.", alias="replicationClusterId")
    run_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the backup run to be triggered by this request. If this is not set defaults to incremental backup.", alias="runType")
    view_id: Optional[StrictInt] = Field(default=None, description="If failover is initiated by view based orchastrator, then this field specifies the local view id of source cluster which is being failed over.", alias="viewId")
    __properties: ClassVar[List[str]] = ["cancelNonFailoverRuns", "objects", "pauseNextRuns", "protectionGroupId", "replicationClusterId", "runType", "viewId"]

    @field_validator('run_type')
    def run_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kAll', 'kHydrateCDP', 'kSystem', 'kStorageArraySnapshot', 'kIncremental', 'kFull', 'kLog']):
            raise ValueError("must be one of enum values ('kAll', 'kHydrateCDP', 'kSystem', 'kStorageArraySnapshot', 'kIncremental', 'kFull', 'kLog')")
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
        """Create an instance of FailoverRunConfiguration from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in objects (list)
        _items = []
        if self.objects:
            for _item_objects in self.objects:
                if _item_objects:
                    _items.append(_item_objects.to_dict())
            _dict['objects'] = _items
        # set to None if cancel_non_failover_runs (nullable) is None
        # and model_fields_set contains the field
        if self.cancel_non_failover_runs is None and "cancel_non_failover_runs" in self.model_fields_set:
            _dict['cancelNonFailoverRuns'] = None

        # set to None if objects (nullable) is None
        # and model_fields_set contains the field
        if self.objects is None and "objects" in self.model_fields_set:
            _dict['objects'] = None

        # set to None if pause_next_runs (nullable) is None
        # and model_fields_set contains the field
        if self.pause_next_runs is None and "pause_next_runs" in self.model_fields_set:
            _dict['pauseNextRuns'] = None

        # set to None if protection_group_id (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_id is None and "protection_group_id" in self.model_fields_set:
            _dict['protectionGroupId'] = None

        # set to None if replication_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.replication_cluster_id is None and "replication_cluster_id" in self.model_fields_set:
            _dict['replicationClusterId'] = None

        # set to None if view_id (nullable) is None
        # and model_fields_set contains the field
        if self.view_id is None and "view_id" in self.model_fields_set:
            _dict['viewId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FailoverRunConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cancelNonFailoverRuns": obj.get("cancelNonFailoverRuns"),
            "objects": [FailoverObject.from_dict(_item) for _item in obj["objects"]] if obj.get("objects") is not None else None,
            "pauseNextRuns": obj.get("pauseNextRuns"),
            "protectionGroupId": obj.get("protectionGroupId"),
            "replicationClusterId": obj.get("replicationClusterId"),
            "runType": obj.get("runType"),
            "viewId": obj.get("viewId")
        })
        return _obj


