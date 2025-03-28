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
from cohesity_sdk.helios.models.helios_search_indexed_objects_cluster_error import HeliosSearchIndexedObjectsClusterError
from typing import Set
from typing_extensions import Self

class HeliosCommonSearchIndexedObjectsResponseParams(BaseModel):
    """
    Specifies the common search indexed objects response params.
    """ # noqa: E501
    cluster_errors: Optional[List[HeliosSearchIndexedObjectsClusterError]] = Field(default=None, description="A List of errors that occured on a subset of clusters.", alias="clusterErrors")
    count: Optional[StrictInt] = Field(default=None, description="Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result.")
    object_type: Optional[StrictStr] = Field(default=None, description="Specifies the object type.", alias="objectType")
    __properties: ClassVar[List[str]] = ["clusterErrors", "count", "objectType"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Emails', 'Files', 'CassandraObjects', 'CouchbaseObjects', 'HbaseObjects', 'HiveObjects', 'MongoObjects', 'HDFSObjects', 'ExchangeObjects', 'PublicFolders', 'GroupsObjects', 'TeamsObjects', 'SharepointObjects', 'OneDriveObjects', 'UdaObjects', 'SfdcRecords']):
            raise ValueError("must be one of enum values ('Emails', 'Files', 'CassandraObjects', 'CouchbaseObjects', 'HbaseObjects', 'HiveObjects', 'MongoObjects', 'HDFSObjects', 'ExchangeObjects', 'PublicFolders', 'GroupsObjects', 'TeamsObjects', 'SharepointObjects', 'OneDriveObjects', 'UdaObjects', 'SfdcRecords')")
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
        """Create an instance of HeliosCommonSearchIndexedObjectsResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_errors (list)
        _items = []
        if self.cluster_errors:
            for _item_cluster_errors in self.cluster_errors:
                if _item_cluster_errors:
                    _items.append(_item_cluster_errors.to_dict())
            _dict['clusterErrors'] = _items
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if object_type (nullable) is None
        # and model_fields_set contains the field
        if self.object_type is None and "object_type" in self.model_fields_set:
            _dict['objectType'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosCommonSearchIndexedObjectsResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterErrors": [HeliosSearchIndexedObjectsClusterError.from_dict(_item) for _item in obj["clusterErrors"]] if obj.get("clusterErrors") is not None else None,
            "count": obj.get("count"),
            "objectType": obj.get("objectType")
        })
        return _obj


