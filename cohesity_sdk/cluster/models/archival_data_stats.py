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
from typing import Optional, Set
from typing_extensions import Self

class ArchivalDataStats(BaseModel):
    """
    Specifies statistics about archival data.
    """ # noqa: E501
    avg_logical_transfer_rate_bps: Optional[StrictInt] = Field(default=None, description="Specifies the average rate of transfer in bytes per second.", alias="avgLogicalTransferRateBps")
    backup_file_count: Optional[StrictInt] = Field(default=None, description="Specifies the total number of file and directory entities that are backed up in this run. Only applicable to file based backups.", alias="backupFileCount")
    bytes_read: Optional[StrictInt] = Field(default=None, description="Specifies total logical bytes read for creating the snapshot.", alias="bytesRead")
    file_walk_done: Optional[StrictBool] = Field(default=None, description="Specifies whether the file system walk is done. Only applicable to file based backups.", alias="fileWalkDone")
    logical_bytes_transferred: Optional[StrictInt] = Field(default=None, description="Specifies the logical bytes transferred.", alias="logicalBytesTransferred")
    logical_size_bytes: Optional[StrictInt] = Field(default=None, description="Specifies the logicalSizeBytes.", alias="logicalSizeBytes")
    physical_bytes_transferred: Optional[StrictInt] = Field(default=None, description="Specifies the physical bytes transferred.", alias="physicalBytesTransferred")
    total_file_count: Optional[StrictInt] = Field(default=None, description="Specifies the total number of file and directory entities visited in this backup. Only applicable to file based backups.", alias="totalFileCount")
    __properties: ClassVar[List[str]] = ["avgLogicalTransferRateBps", "backupFileCount", "bytesRead", "fileWalkDone", "logicalBytesTransferred", "logicalSizeBytes", "physicalBytesTransferred", "totalFileCount"]

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
        """Create an instance of ArchivalDataStats from a JSON string"""
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
        # set to None if avg_logical_transfer_rate_bps (nullable) is None
        # and model_fields_set contains the field
        if self.avg_logical_transfer_rate_bps is None and "avg_logical_transfer_rate_bps" in self.model_fields_set:
            _dict['avgLogicalTransferRateBps'] = None

        # set to None if backup_file_count (nullable) is None
        # and model_fields_set contains the field
        if self.backup_file_count is None and "backup_file_count" in self.model_fields_set:
            _dict['backupFileCount'] = None

        # set to None if bytes_read (nullable) is None
        # and model_fields_set contains the field
        if self.bytes_read is None and "bytes_read" in self.model_fields_set:
            _dict['bytesRead'] = None

        # set to None if file_walk_done (nullable) is None
        # and model_fields_set contains the field
        if self.file_walk_done is None and "file_walk_done" in self.model_fields_set:
            _dict['fileWalkDone'] = None

        # set to None if logical_bytes_transferred (nullable) is None
        # and model_fields_set contains the field
        if self.logical_bytes_transferred is None and "logical_bytes_transferred" in self.model_fields_set:
            _dict['logicalBytesTransferred'] = None

        # set to None if logical_size_bytes (nullable) is None
        # and model_fields_set contains the field
        if self.logical_size_bytes is None and "logical_size_bytes" in self.model_fields_set:
            _dict['logicalSizeBytes'] = None

        # set to None if physical_bytes_transferred (nullable) is None
        # and model_fields_set contains the field
        if self.physical_bytes_transferred is None and "physical_bytes_transferred" in self.model_fields_set:
            _dict['physicalBytesTransferred'] = None

        # set to None if total_file_count (nullable) is None
        # and model_fields_set contains the field
        if self.total_file_count is None and "total_file_count" in self.model_fields_set:
            _dict['totalFileCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ArchivalDataStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "avgLogicalTransferRateBps": obj.get("avgLogicalTransferRateBps"),
            "backupFileCount": obj.get("backupFileCount"),
            "bytesRead": obj.get("bytesRead"),
            "fileWalkDone": obj.get("fileWalkDone"),
            "logicalBytesTransferred": obj.get("logicalBytesTransferred"),
            "logicalSizeBytes": obj.get("logicalSizeBytes"),
            "physicalBytesTransferred": obj.get("physicalBytesTransferred"),
            "totalFileCount": obj.get("totalFileCount")
        })
        return _obj


