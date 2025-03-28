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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.cassandra_search_params import CassandraSearchParams
from cohesity_sdk.helios.models.couchbase_search_params import CouchbaseSearchParams
from cohesity_sdk.helios.models.email_helios_search_params import EmailHeliosSearchParams
from cohesity_sdk.helios.models.hbase_search_params import HbaseSearchParams
from cohesity_sdk.helios.models.hdfs_search_params import HdfsSearchParams
from cohesity_sdk.helios.models.hive_search_params import HiveSearchParams
from cohesity_sdk.helios.models.mongodb_search_params import MongodbSearchParams
from cohesity_sdk.helios.models.search_exchange_objects_request_params import SearchExchangeObjectsRequestParams
from cohesity_sdk.helios.models.search_file_request_params_base import SearchFileRequestParamsBase
from cohesity_sdk.helios.models.search_ms_groups_request_params import SearchMsGroupsRequestParams
from cohesity_sdk.helios.models.search_ms_teams_request_params import SearchMsTeamsRequestParams
from cohesity_sdk.helios.models.search_public_folder_request_params import SearchPublicFolderRequestParams
from cohesity_sdk.helios.models.search_sfdc_records_request_params import SearchSfdcRecordsRequestParams
from cohesity_sdk.helios.models.uda_search_params import UdaSearchParams
from typing import Set
from typing_extensions import Self

class HeliosSearchIndexedObjectsRequest(BaseModel):
    """
    Specifies the request parameters to search for global indexed objects.
    """ # noqa: E501
    cluster_identifiers: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId.", alias="clusterIdentifiers")
    count: Optional[StrictInt] = Field(default=None, description="Specifies the number of indexed objects to be fetched.")
    object_type: Optional[StrictStr] = Field(description="Specifies the object type to be searched for.", alias="objectType")
    region_ids: Optional[List[StrictStr]] = Field(default=None, description="List of Regions to filter from.", alias="regionIds")
    source_uuids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of source UUIDs. Only matches found in these sources will be returned.", alias="sourceUUIDs")
    cassandra_params: Optional[CassandraSearchParams] = Field(default=None, alias="cassandraParams")
    couchbase_params: Optional[CouchbaseSearchParams] = Field(default=None, alias="couchbaseParams")
    email_params: Optional[EmailHeliosSearchParams] = Field(default=None, alias="emailParams")
    exchange_params: Optional[SearchExchangeObjectsRequestParams] = Field(default=None, alias="exchangeParams")
    file_params: Optional[SearchFileRequestParamsBase] = Field(default=None, alias="fileParams")
    hbase_params: Optional[HbaseSearchParams] = Field(default=None, alias="hbaseParams")
    hdfs_params: Optional[HdfsSearchParams] = Field(default=None, alias="hdfsParams")
    hive_params: Optional[HiveSearchParams] = Field(default=None, alias="hiveParams")
    mongodb_params: Optional[MongodbSearchParams] = Field(default=None, alias="mongodbParams")
    ms_groups_params: Optional[SearchMsGroupsRequestParams] = Field(default=None, alias="msGroupsParams")
    ms_teams_params: Optional[SearchMsTeamsRequestParams] = Field(default=None, alias="msTeamsParams")
    public_folder_params: Optional[SearchPublicFolderRequestParams] = Field(default=None, alias="publicFolderParams")
    sfdc_params: Optional[SearchSfdcRecordsRequestParams] = Field(default=None, alias="sfdcParams")
    uda_params: Optional[UdaSearchParams] = Field(default=None, alias="udaParams")
    __properties: ClassVar[List[str]] = ["clusterIdentifiers", "count", "objectType", "regionIds", "sourceUUIDs", "cassandraParams", "couchbaseParams", "emailParams", "exchangeParams", "fileParams", "hbaseParams", "hdfsParams", "hiveParams", "mongodbParams", "msGroupsParams", "msTeamsParams", "publicFolderParams", "sfdcParams", "udaParams"]

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
        """Create an instance of HeliosSearchIndexedObjectsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cassandra_params
        if self.cassandra_params:
            _dict['cassandraParams'] = self.cassandra_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of couchbase_params
        if self.couchbase_params:
            _dict['couchbaseParams'] = self.couchbase_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email_params
        if self.email_params:
            _dict['emailParams'] = self.email_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of exchange_params
        if self.exchange_params:
            _dict['exchangeParams'] = self.exchange_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of file_params
        if self.file_params:
            _dict['fileParams'] = self.file_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hbase_params
        if self.hbase_params:
            _dict['hbaseParams'] = self.hbase_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hdfs_params
        if self.hdfs_params:
            _dict['hdfsParams'] = self.hdfs_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of hive_params
        if self.hive_params:
            _dict['hiveParams'] = self.hive_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mongodb_params
        if self.mongodb_params:
            _dict['mongodbParams'] = self.mongodb_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ms_groups_params
        if self.ms_groups_params:
            _dict['msGroupsParams'] = self.ms_groups_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ms_teams_params
        if self.ms_teams_params:
            _dict['msTeamsParams'] = self.ms_teams_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_folder_params
        if self.public_folder_params:
            _dict['publicFolderParams'] = self.public_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # set to None if cluster_identifiers (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_identifiers is None and "cluster_identifiers" in self.model_fields_set:
            _dict['clusterIdentifiers'] = None

        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if object_type (nullable) is None
        # and model_fields_set contains the field
        if self.object_type is None and "object_type" in self.model_fields_set:
            _dict['objectType'] = None

        # set to None if region_ids (nullable) is None
        # and model_fields_set contains the field
        if self.region_ids is None and "region_ids" in self.model_fields_set:
            _dict['regionIds'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeliosSearchIndexedObjectsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterIdentifiers": obj.get("clusterIdentifiers"),
            "count": obj.get("count"),
            "objectType": obj.get("objectType"),
            "regionIds": obj.get("regionIds"),
            "sourceUUIDs": obj.get("sourceUUIDs"),
            "cassandraParams": CassandraSearchParams.from_dict(obj["cassandraParams"]) if obj.get("cassandraParams") is not None else None,
            "couchbaseParams": CouchbaseSearchParams.from_dict(obj["couchbaseParams"]) if obj.get("couchbaseParams") is not None else None,
            "emailParams": EmailHeliosSearchParams.from_dict(obj["emailParams"]) if obj.get("emailParams") is not None else None,
            "exchangeParams": SearchExchangeObjectsRequestParams.from_dict(obj["exchangeParams"]) if obj.get("exchangeParams") is not None else None,
            "fileParams": SearchFileRequestParamsBase.from_dict(obj["fileParams"]) if obj.get("fileParams") is not None else None,
            "hbaseParams": HbaseSearchParams.from_dict(obj["hbaseParams"]) if obj.get("hbaseParams") is not None else None,
            "hdfsParams": HdfsSearchParams.from_dict(obj["hdfsParams"]) if obj.get("hdfsParams") is not None else None,
            "hiveParams": HiveSearchParams.from_dict(obj["hiveParams"]) if obj.get("hiveParams") is not None else None,
            "mongodbParams": MongodbSearchParams.from_dict(obj["mongodbParams"]) if obj.get("mongodbParams") is not None else None,
            "msGroupsParams": SearchMsGroupsRequestParams.from_dict(obj["msGroupsParams"]) if obj.get("msGroupsParams") is not None else None,
            "msTeamsParams": SearchMsTeamsRequestParams.from_dict(obj["msTeamsParams"]) if obj.get("msTeamsParams") is not None else None,
            "publicFolderParams": SearchPublicFolderRequestParams.from_dict(obj["publicFolderParams"]) if obj.get("publicFolderParams") is not None else None,
            "sfdcParams": SearchSfdcRecordsRequestParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "udaParams": UdaSearchParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None
        })
        return _obj


