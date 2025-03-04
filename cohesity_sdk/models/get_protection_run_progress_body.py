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
from cohesity_sdk.models.archival_target_progress_info import ArchivalTargetProgressInfo
from cohesity_sdk.models.backup_run_progress_info import BackupRunProgressInfo
from cohesity_sdk.models.replication_target_progress_info import ReplicationTargetProgressInfo
from typing import Optional, Set
from typing_extensions import Self

class GetProtectionRunProgressBody(BaseModel):
    """
    Specifies the progress of a protection run.
    """ # noqa: E501
    archival_run: Optional[List[ArchivalTargetProgressInfo]] = Field(default=None, description="Progress for the archival run.", alias="archivalRun")
    local_run: Optional[BackupRunProgressInfo] = Field(default=None, alias="localRun")
    replication_run: Optional[List[ReplicationTargetProgressInfo]] = Field(default=None, description="Progress for the replication run.", alias="replicationRun")
    __properties: ClassVar[List[str]] = ["archivalRun", "localRun", "replicationRun"]

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
        """Create an instance of GetProtectionRunProgressBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in archival_run (list)
        _items = []
        if self.archival_run:
            for _item_archival_run in self.archival_run:
                if _item_archival_run:
                    _items.append(_item_archival_run.to_dict())
            _dict['archivalRun'] = _items
        # override the default output from pydantic by calling `to_dict()` of local_run
        if self.local_run:
            _dict['localRun'] = self.local_run.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in replication_run (list)
        _items = []
        if self.replication_run:
            for _item_replication_run in self.replication_run:
                if _item_replication_run:
                    _items.append(_item_replication_run.to_dict())
            _dict['replicationRun'] = _items
        # set to None if archival_run (nullable) is None
        # and model_fields_set contains the field
        if self.archival_run is None and "archival_run" in self.model_fields_set:
            _dict['archivalRun'] = None

        # set to None if replication_run (nullable) is None
        # and model_fields_set contains the field
        if self.replication_run is None and "replication_run" in self.model_fields_set:
            _dict['replicationRun'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetProtectionRunProgressBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "archivalRun": [ArchivalTargetProgressInfo.from_dict(_item) for _item in obj["archivalRun"]] if obj.get("archivalRun") is not None else None,
            "localRun": BackupRunProgressInfo.from_dict(obj["localRun"]) if obj.get("localRun") is not None else None,
            "replicationRun": [ReplicationTargetProgressInfo.from_dict(_item) for _item in obj["replicationRun"]] if obj.get("replicationRun") is not None else None
        })
        return _obj


