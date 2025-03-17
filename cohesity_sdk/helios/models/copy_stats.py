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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.anomaly_status import AnomalyStatus
from cohesity_sdk.helios.models.archival_copy import ArchivalCopy
from cohesity_sdk.helios.models.file_extension_details import FileExtensionDetails
from cohesity_sdk.helios.models.indexing_stats import IndexingStats
from cohesity_sdk.helios.models.local_copy import LocalCopy
from cohesity_sdk.helios.models.replication_copy import ReplicationCopy
from cohesity_sdk.helios.models.storage_metrics import StorageMetrics
from cohesity_sdk.helios.models.tags import Tags
from typing import Set
from typing_extensions import Self

class CopyStats(BaseModel):
    """
    Specifies the stats for all the copies of this backup run.
    """ # noqa: E501
    anomaly_status: Optional[AnomalyStatus] = Field(default=None, alias="anomalyStatus")
    archivals: Optional[List[ArchivalCopy]] = Field(default=None, description="This contains the details of the archival copies of the run.")
    file_extensions: Optional[List[FileExtensionDetails]] = Field(default=None, alias="fileExtensions")
    indexing_stats: Optional[IndexingStats] = Field(default=None, alias="indexingStats")
    local: Optional[LocalCopy] = None
    page_count: Optional[StrictInt] = Field(default=None, description="The page count of this response.", alias="pageCount")
    page_size: Optional[StrictInt] = Field(default=None, description="The page size of this result.", alias="pageSize")
    replications: Optional[List[ReplicationCopy]] = Field(default=None, description="Replication copies of the run.")
    storage_metrics: Optional[StorageMetrics] = Field(default=None, alias="storageMetrics")
    tagging_info: Optional[Tags] = Field(default=None, alias="taggingInfo")
    __properties: ClassVar[List[str]] = ["anomalyStatus", "archivals", "fileExtensions", "indexingStats", "local", "pageCount", "pageSize", "replications", "storageMetrics", "taggingInfo"]

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
        """Create an instance of CopyStats from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anomaly_status
        if self.anomaly_status:
            _dict['anomalyStatus'] = self.anomaly_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in archivals (list)
        _items = []
        if self.archivals:
            for _item_archivals in self.archivals:
                if _item_archivals:
                    _items.append(_item_archivals.to_dict())
            _dict['archivals'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in file_extensions (list)
        _items = []
        if self.file_extensions:
            for _item_file_extensions in self.file_extensions:
                if _item_file_extensions:
                    _items.append(_item_file_extensions.to_dict())
            _dict['fileExtensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of indexing_stats
        if self.indexing_stats:
            _dict['indexingStats'] = self.indexing_stats.to_dict()
        # override the default output from pydantic by calling `to_dict()` of local
        if self.local:
            _dict['local'] = self.local.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in replications (list)
        _items = []
        if self.replications:
            for _item_replications in self.replications:
                if _item_replications:
                    _items.append(_item_replications.to_dict())
            _dict['replications'] = _items
        # override the default output from pydantic by calling `to_dict()` of storage_metrics
        if self.storage_metrics:
            _dict['storageMetrics'] = self.storage_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tagging_info
        if self.tagging_info:
            _dict['taggingInfo'] = self.tagging_info.to_dict()
        # set to None if page_count (nullable) is None
        # and model_fields_set contains the field
        if self.page_count is None and "page_count" in self.model_fields_set:
            _dict['pageCount'] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict['pageSize'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CopyStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anomalyStatus": AnomalyStatus.from_dict(obj["anomalyStatus"]) if obj.get("anomalyStatus") is not None else None,
            "archivals": [ArchivalCopy.from_dict(_item) for _item in obj["archivals"]] if obj.get("archivals") is not None else None,
            "fileExtensions": [FileExtensionDetails.from_dict(_item) for _item in obj["fileExtensions"]] if obj.get("fileExtensions") is not None else None,
            "indexingStats": IndexingStats.from_dict(obj["indexingStats"]) if obj.get("indexingStats") is not None else None,
            "local": LocalCopy.from_dict(obj["local"]) if obj.get("local") is not None else None,
            "pageCount": obj.get("pageCount"),
            "pageSize": obj.get("pageSize"),
            "replications": [ReplicationCopy.from_dict(_item) for _item in obj["replications"]] if obj.get("replications") is not None else None,
            "storageMetrics": StorageMetrics.from_dict(obj["storageMetrics"]) if obj.get("storageMetrics") is not None else None,
            "taggingInfo": Tags.from_dict(obj["taggingInfo"]) if obj.get("taggingInfo") is not None else None
        })
        return _obj


