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
from cohesity_sdk.cluster.models.run_replication_config import RunReplicationConfig
from cohesity_sdk.cluster.models.update_existing_replication_snapshot_config import UpdateExistingReplicationSnapshotConfig
from typing import Optional, Set
from typing_extensions import Self

class UpdateReplicationSnapshotConfig(BaseModel):
    """
    Specifies the params to perform actions on replication snapshots taken by a Protection Group Run.
    """ # noqa: E501
    new_snapshot_config: Optional[List[RunReplicationConfig]] = Field(default=None, description="Specifies the new configuration about adding Replication Snapshot to existing Protection Group Run.", alias="newSnapshotConfig")
    update_existing_snapshot_config: Optional[List[UpdateExistingReplicationSnapshotConfig]] = Field(default=None, description="Specifies the configuration about updating an existing Replication Snapshot Run.", alias="updateExistingSnapshotConfig")
    __properties: ClassVar[List[str]] = ["newSnapshotConfig", "updateExistingSnapshotConfig"]

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
        """Create an instance of UpdateReplicationSnapshotConfig from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in new_snapshot_config (list)
        _items = []
        if self.new_snapshot_config:
            for _item_new_snapshot_config in self.new_snapshot_config:
                if _item_new_snapshot_config:
                    _items.append(_item_new_snapshot_config.to_dict())
            _dict['newSnapshotConfig'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in update_existing_snapshot_config (list)
        _items = []
        if self.update_existing_snapshot_config:
            for _item_update_existing_snapshot_config in self.update_existing_snapshot_config:
                if _item_update_existing_snapshot_config:
                    _items.append(_item_update_existing_snapshot_config.to_dict())
            _dict['updateExistingSnapshotConfig'] = _items
        # set to None if new_snapshot_config (nullable) is None
        # and model_fields_set contains the field
        if self.new_snapshot_config is None and "new_snapshot_config" in self.model_fields_set:
            _dict['newSnapshotConfig'] = None

        # set to None if update_existing_snapshot_config (nullable) is None
        # and model_fields_set contains the field
        if self.update_existing_snapshot_config is None and "update_existing_snapshot_config" in self.model_fields_set:
            _dict['updateExistingSnapshotConfig'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateReplicationSnapshotConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "newSnapshotConfig": [RunReplicationConfig.from_dict(_item) for _item in obj["newSnapshotConfig"]] if obj.get("newSnapshotConfig") is not None else None,
            "updateExistingSnapshotConfig": [UpdateExistingReplicationSnapshotConfig.from_dict(_item) for _item in obj["updateExistingSnapshotConfig"]] if obj.get("updateExistingSnapshotConfig") is not None else None
        })
        return _obj


