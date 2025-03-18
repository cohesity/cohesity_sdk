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
from cohesity_sdk.helios.models.snapshot_tag import SnapshotTag
from typing import Set
from typing_extensions import Self

class GetCopyStatParams(BaseModel):
    """
    GetCopyStatParams
    """ # noqa: E501
    cluster_identifiers: Optional[List[StrictStr]] = Field(default=None, description="This is a list of cluster identifiers to query snapshots for", alias="clusterIdentifiers")
    from_run_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started after this value.", alias="fromRunStartTimeUsecs")
    has_anomaly_tag: Optional[StrictBool] = Field(default=None, description="This is a boolean to indicate if there are any anomaly tags on this run.", alias="hasAnomalyTag")
    locations: Optional[List[StrictStr]] = Field(default=None, description="This is to filter the type of runs to return.")
    object_ids: Optional[List[StrictInt]] = Field(default=None, description="List of object ids to filter results.", alias="objectIds")
    page_count: Optional[StrictInt] = Field(default=None, description="Each result is returned in pages. This is the page number of the requested result. This parameters starts from 0.", alias="pageCount")
    page_size: Optional[StrictInt] = Field(default=None, description="The number of results to include in a page.", alias="pageSize")
    protection_group_ids: Optional[List[StrictStr]] = Field(default=None, description="This parameter applies if a single cluster is passed in cluster identifiers.", alias="protectionGroupIds")
    region_ids: Optional[List[StrictStr]] = Field(default=None, description="List of region Ids.", alias="regionIds")
    requested_data: Optional[List[StrictStr]] = Field(default=None, description="Filter out the type data requested per run.", alias="requestedData")
    run_instance_ids: Optional[List[StrictInt]] = Field(default=None, description="This parameter applies if a single cluster is passed in cluster identifiers.", alias="runInstanceIds")
    snapshot_ids: Optional[List[StrictStr]] = Field(default=None, description="List of snapshots Ids to filter result.", alias="snapshotIds")
    tags: Optional[List[SnapshotTag]] = Field(default=None, description="List of tags to filter.")
    tenant_ids: Optional[List[StrictStr]] = Field(default=None, description="List of tenant ids in an account.", alias="tenantIds")
    to_run_start_time_usecs: Optional[StrictInt] = Field(default=None, description="Specifies the timestamp in Unix time epoch in microseconds to filter snapshots whose corresponding run started before this value.", alias="toRunStartTimeUsecs")
    __properties: ClassVar[List[str]] = ["clusterIdentifiers", "fromRunStartTimeUsecs", "hasAnomalyTag", "locations", "objectIds", "pageCount", "pageSize", "protectionGroupIds", "regionIds", "requestedData", "runInstanceIds", "snapshotIds", "tags", "tenantIds", "toRunStartTimeUsecs"]

    @field_validator('locations')
    def locations_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['cluster', 'archival', 'replication']):
                raise ValueError("each list item must be one of ('cluster', 'archival', 'replication')")
        return value

    @field_validator('requested_data')
    def requested_data_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['storageMetrics', 'indexingStats', 'taggingInfo']):
                raise ValueError("each list item must be one of ('storageMetrics', 'indexingStats', 'taggingInfo')")
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
        """Create an instance of GetCopyStatParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # set to None if cluster_identifiers (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_identifiers is None and "cluster_identifiers" in self.model_fields_set:
            _dict['clusterIdentifiers'] = None

        # set to None if has_anomaly_tag (nullable) is None
        # and model_fields_set contains the field
        if self.has_anomaly_tag is None and "has_anomaly_tag" in self.model_fields_set:
            _dict['hasAnomalyTag'] = None

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
        """Create an instance of GetCopyStatParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterIdentifiers": obj.get("clusterIdentifiers"),
            "fromRunStartTimeUsecs": obj.get("fromRunStartTimeUsecs"),
            "hasAnomalyTag": obj.get("hasAnomalyTag"),
            "locations": obj.get("locations"),
            "objectIds": obj.get("objectIds"),
            "pageCount": obj.get("pageCount"),
            "pageSize": obj.get("pageSize"),
            "protectionGroupIds": obj.get("protectionGroupIds"),
            "regionIds": obj.get("regionIds"),
            "requestedData": obj.get("requestedData"),
            "runInstanceIds": obj.get("runInstanceIds"),
            "snapshotIds": obj.get("snapshotIds"),
            "tags": [SnapshotTag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "tenantIds": obj.get("tenantIds"),
            "toRunStartTimeUsecs": obj.get("toRunStartTimeUsecs")
        })
        return _obj


