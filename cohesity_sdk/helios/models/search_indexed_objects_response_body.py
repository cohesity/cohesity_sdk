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
from cohesity_sdk.helios.models.cassandra_indexed_object import CassandraIndexedObject
from cohesity_sdk.helios.models.couchbase_indexed_object import CouchbaseIndexedObject
from cohesity_sdk.helios.models.document_library_item import DocumentLibraryItem
from cohesity_sdk.helios.models.email import Email
from cohesity_sdk.helios.models.exchange_indexed_object import ExchangeIndexedObject
from cohesity_sdk.helios.models.file import File
from cohesity_sdk.helios.models.hbase_indexed_object import HbaseIndexedObject
from cohesity_sdk.helios.models.hdfs_indexed_object import HDFSIndexedObject
from cohesity_sdk.helios.models.hive_indexed_object import HiveIndexedObject
from cohesity_sdk.helios.models.mongo_indexed_object import MongoIndexedObject
from cohesity_sdk.helios.models.ms_group_item import MsGroupItem
from cohesity_sdk.helios.models.public_folder_item import PublicFolderItem
from cohesity_sdk.helios.models.sfdc_records import SfdcRecords
from cohesity_sdk.helios.models.sharepoint_item import SharepointItem
from cohesity_sdk.helios.models.teams_item import TeamsItem
from cohesity_sdk.helios.models.uda_indexed_object import UdaIndexedObject
from typing import Set
from typing_extensions import Self

class SearchIndexedObjectsResponseBody(BaseModel):
    """
    Specifies the search indexed objects response body.
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Specifies the total number of indexed objects that match the filter and search criteria. Use this value to determine how many additional requests are required to get the full result.")
    object_type: Optional[StrictStr] = Field(default=None, description="Specifies the object type.", alias="objectType")
    pagination_cookie: Optional[StrictStr] = Field(default=None, description="Specifies cookie for resuming search if pagination is being used.", alias="paginationCookie")
    cassandra_objects: Optional[List[CassandraIndexedObject]] = Field(default=None, description="Specifies the indexed Cassandra objects.", alias="cassandraObjects")
    couchbase_objects: Optional[List[CouchbaseIndexedObject]] = Field(default=None, description="Specifies the indexed Couchbase objects.", alias="couchbaseObjects")
    emails: Optional[List[Email]] = Field(default=None, description="Specifies the indexed emails and email folders.")
    exchange_objects: Optional[List[ExchangeIndexedObject]] = Field(default=None, description="Specifies the indexed HDFS objects.", alias="exchangeObjects")
    files: Optional[List[File]] = Field(default=None, description="Specifies the indexed files.")
    hbase_objects: Optional[List[HbaseIndexedObject]] = Field(default=None, description="Specifies the indexed Hbase objects.", alias="hbaseObjects")
    hdfs_objects: Optional[List[HDFSIndexedObject]] = Field(default=None, description="Specifies the indexed HDFS objects.", alias="hdfsObjects")
    hive_objects: Optional[List[HiveIndexedObject]] = Field(default=None, description="Specifies the indexed Hive objects.", alias="hiveObjects")
    mongo_objects: Optional[List[MongoIndexedObject]] = Field(default=None, description="Specifies the indexed Mongo objects.", alias="mongoObjects")
    ms_group_items: Optional[List[MsGroupItem]] = Field(default=None, description="Specifies the indexed M365 Groups items like group mail items, files etc.", alias="msGroupItems")
    one_drive_items: Optional[List[DocumentLibraryItem]] = Field(default=None, description="Specifies the indexed one drive items.", alias="oneDriveItems")
    public_folder_items: Optional[List[PublicFolderItem]] = Field(default=None, description="Specifies the indexed Public folder items.", alias="publicFolderItems")
    sfdc_records: Optional[SfdcRecords] = Field(default=None, alias="sfdcRecords")
    sharepoint_items: Optional[List[SharepointItem]] = Field(default=None, description="Specifies the indexed Sharepoint items.", alias="sharepointItems")
    teams_items: Optional[List[TeamsItem]] = Field(default=None, description="Specifies the indexed M365 Teams items like channels, files etc.", alias="teamsItems")
    uda_objects: Optional[List[UdaIndexedObject]] = Field(default=None, description="Specifies the indexed Universal Data Adapter objects.", alias="udaObjects")
    __properties: ClassVar[List[str]] = ["count", "objectType", "paginationCookie", "cassandraObjects", "couchbaseObjects", "emails", "exchangeObjects", "files", "hbaseObjects", "hdfsObjects", "hiveObjects", "mongoObjects", "msGroupItems", "oneDriveItems", "publicFolderItems", "sfdcRecords", "sharepointItems", "teamsItems", "udaObjects"]

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
        """Create an instance of SearchIndexedObjectsResponseBody from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in cassandra_objects (list)
        _items = []
        if self.cassandra_objects:
            for _item_cassandra_objects in self.cassandra_objects:
                if _item_cassandra_objects:
                    _items.append(_item_cassandra_objects.to_dict())
            _dict['cassandraObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in couchbase_objects (list)
        _items = []
        if self.couchbase_objects:
            for _item_couchbase_objects in self.couchbase_objects:
                if _item_couchbase_objects:
                    _items.append(_item_couchbase_objects.to_dict())
            _dict['couchbaseObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in emails (list)
        _items = []
        if self.emails:
            for _item_emails in self.emails:
                if _item_emails:
                    _items.append(_item_emails.to_dict())
            _dict['emails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in exchange_objects (list)
        _items = []
        if self.exchange_objects:
            for _item_exchange_objects in self.exchange_objects:
                if _item_exchange_objects:
                    _items.append(_item_exchange_objects.to_dict())
            _dict['exchangeObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item_files in self.files:
                if _item_files:
                    _items.append(_item_files.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hbase_objects (list)
        _items = []
        if self.hbase_objects:
            for _item_hbase_objects in self.hbase_objects:
                if _item_hbase_objects:
                    _items.append(_item_hbase_objects.to_dict())
            _dict['hbaseObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hdfs_objects (list)
        _items = []
        if self.hdfs_objects:
            for _item_hdfs_objects in self.hdfs_objects:
                if _item_hdfs_objects:
                    _items.append(_item_hdfs_objects.to_dict())
            _dict['hdfsObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in hive_objects (list)
        _items = []
        if self.hive_objects:
            for _item_hive_objects in self.hive_objects:
                if _item_hive_objects:
                    _items.append(_item_hive_objects.to_dict())
            _dict['hiveObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mongo_objects (list)
        _items = []
        if self.mongo_objects:
            for _item_mongo_objects in self.mongo_objects:
                if _item_mongo_objects:
                    _items.append(_item_mongo_objects.to_dict())
            _dict['mongoObjects'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ms_group_items (list)
        _items = []
        if self.ms_group_items:
            for _item_ms_group_items in self.ms_group_items:
                if _item_ms_group_items:
                    _items.append(_item_ms_group_items.to_dict())
            _dict['msGroupItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in one_drive_items (list)
        _items = []
        if self.one_drive_items:
            for _item_one_drive_items in self.one_drive_items:
                if _item_one_drive_items:
                    _items.append(_item_one_drive_items.to_dict())
            _dict['oneDriveItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in public_folder_items (list)
        _items = []
        if self.public_folder_items:
            for _item_public_folder_items in self.public_folder_items:
                if _item_public_folder_items:
                    _items.append(_item_public_folder_items.to_dict())
            _dict['publicFolderItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of sfdc_records
        if self.sfdc_records:
            _dict['sfdcRecords'] = self.sfdc_records.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sharepoint_items (list)
        _items = []
        if self.sharepoint_items:
            for _item_sharepoint_items in self.sharepoint_items:
                if _item_sharepoint_items:
                    _items.append(_item_sharepoint_items.to_dict())
            _dict['sharepointItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in teams_items (list)
        _items = []
        if self.teams_items:
            for _item_teams_items in self.teams_items:
                if _item_teams_items:
                    _items.append(_item_teams_items.to_dict())
            _dict['teamsItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in uda_objects (list)
        _items = []
        if self.uda_objects:
            for _item_uda_objects in self.uda_objects:
                if _item_uda_objects:
                    _items.append(_item_uda_objects.to_dict())
            _dict['udaObjects'] = _items
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if pagination_cookie (nullable) is None
        # and model_fields_set contains the field
        if self.pagination_cookie is None and "pagination_cookie" in self.model_fields_set:
            _dict['paginationCookie'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchIndexedObjectsResponseBody from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "objectType": obj.get("objectType"),
            "paginationCookie": obj.get("paginationCookie"),
            "cassandraObjects": [CassandraIndexedObject.from_dict(_item) for _item in obj["cassandraObjects"]] if obj.get("cassandraObjects") is not None else None,
            "couchbaseObjects": [CouchbaseIndexedObject.from_dict(_item) for _item in obj["couchbaseObjects"]] if obj.get("couchbaseObjects") is not None else None,
            "emails": [Email.from_dict(_item) for _item in obj["emails"]] if obj.get("emails") is not None else None,
            "exchangeObjects": [ExchangeIndexedObject.from_dict(_item) for _item in obj["exchangeObjects"]] if obj.get("exchangeObjects") is not None else None,
            "files": [File.from_dict(_item) for _item in obj["files"]] if obj.get("files") is not None else None,
            "hbaseObjects": [HbaseIndexedObject.from_dict(_item) for _item in obj["hbaseObjects"]] if obj.get("hbaseObjects") is not None else None,
            "hdfsObjects": [HDFSIndexedObject.from_dict(_item) for _item in obj["hdfsObjects"]] if obj.get("hdfsObjects") is not None else None,
            "hiveObjects": [HiveIndexedObject.from_dict(_item) for _item in obj["hiveObjects"]] if obj.get("hiveObjects") is not None else None,
            "mongoObjects": [MongoIndexedObject.from_dict(_item) for _item in obj["mongoObjects"]] if obj.get("mongoObjects") is not None else None,
            "msGroupItems": [MsGroupItem.from_dict(_item) for _item in obj["msGroupItems"]] if obj.get("msGroupItems") is not None else None,
            "oneDriveItems": [DocumentLibraryItem.from_dict(_item) for _item in obj["oneDriveItems"]] if obj.get("oneDriveItems") is not None else None,
            "publicFolderItems": [PublicFolderItem.from_dict(_item) for _item in obj["publicFolderItems"]] if obj.get("publicFolderItems") is not None else None,
            "sfdcRecords": SfdcRecords.from_dict(obj["sfdcRecords"]) if obj.get("sfdcRecords") is not None else None,
            "sharepointItems": [SharepointItem.from_dict(_item) for _item in obj["sharepointItems"]] if obj.get("sharepointItems") is not None else None,
            "teamsItems": [TeamsItem.from_dict(_item) for _item in obj["teamsItems"]] if obj.get("teamsItems") is not None else None,
            "udaObjects": [UdaIndexedObject.from_dict(_item) for _item in obj["udaObjects"]] if obj.get("udaObjects") is not None else None
        })
        return _obj


