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
from typing_extensions import Annotated
from cohesity_sdk.helios.models.cassandra_on_prem_search_params import CassandraOnPremSearchParams
from cohesity_sdk.helios.models.couch_base_on_prem_search_params import CouchBaseOnPremSearchParams
from cohesity_sdk.helios.models.hbase_on_prem_search_params import HbaseOnPremSearchParams
from cohesity_sdk.helios.models.hdfson_prem_search_params import HDFSOnPremSearchParams
from cohesity_sdk.helios.models.hive_on_prem_search_params import HiveOnPremSearchParams
from cohesity_sdk.helios.models.mongo_db_on_prem_search_params import MongoDbOnPremSearchParams
from cohesity_sdk.helios.models.search_document_library_request_params import SearchDocumentLibraryRequestParams
from cohesity_sdk.helios.models.search_email_request_params import SearchEmailRequestParams
from cohesity_sdk.helios.models.search_exchange_objects_request_params import SearchExchangeObjectsRequestParams
from cohesity_sdk.helios.models.search_file_request_params import SearchFileRequestParams
from cohesity_sdk.helios.models.search_ms_groups_request_params import SearchMsGroupsRequestParams
from cohesity_sdk.helios.models.search_ms_teams_request_params import SearchMsTeamsRequestParams
from cohesity_sdk.helios.models.search_public_folder_request_params import SearchPublicFolderRequestParams
from cohesity_sdk.helios.models.search_sfdc_records_request_params import SearchSfdcRecordsRequestParams
from cohesity_sdk.helios.models.uda_on_prem_search_params import UdaOnPremSearchParams
from typing import Optional, Set
from typing_extensions import Self

class SearchIndexedObjectsRequest(BaseModel):
    """
    Specifies the request parameters to search for indexed objects.
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Specifies the number of indexed objects to be fetched for the specified pagination cookie.")
    include_tenants: Optional[StrictBool] = Field(default=False, description="If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false.", alias="includeTenants")
    might_have_snapshot_tag_ids: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Specifies list of snapshot tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query.", alias="mightHaveSnapshotTagIds")
    might_have_tag_ids: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Specifies list of tags, one or more of which might be present in the document. These are OR'ed together and the resulting criteria AND'ed with the rest of the query.", alias="mightHaveTagIds")
    must_have_snapshot_tag_ids: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Specifies snapshot tags which must be all present in the document.", alias="mustHaveSnapshotTagIds")
    must_have_tag_ids: Optional[List[Annotated[str, Field(strict=True)]]] = Field(default=None, description="Specifies tags which must be all present in the document.", alias="mustHaveTagIds")
    object_type: StrictStr = Field(description="Specifies the object type to be searched for.", alias="objectType")
    pagination_cookie: Optional[StrictStr] = Field(default=None, description="Specifies the pagination cookie with which subsequent parts of the response can be fetched.", alias="paginationCookie")
    protection_group_ids: Optional[List[StrictStr]] = Field(default=None, description="Specifies a list of Protection Group ids to filter the indexed objects. If specified, the objects indexed by specified Protection Group ids will be returned.", alias="protectionGroupIds")
    snapshot_tags: Optional[List[StrictStr]] = Field(default=None, description="\"This field is deprecated. Please use mightHaveSnapshotTagIds.\"", alias="snapshotTags")
    storage_domain_ids: Optional[List[StrictInt]] = Field(default=None, description="Specifies the Storage Domain ids to filter indexed objects for which Protection Groups are writing data to Cohesity Views on the specified Storage Domains.", alias="storageDomainIds")
    tags: Optional[List[StrictStr]] = Field(default=None, description="\"This field is deprecated. Please use mightHaveTagIds.\"")
    tenant_id: Optional[StrictStr] = Field(default=None, description="TenantId contains id of the tenant for which objects are to be returned.", alias="tenantId")
    use_cached_data: Optional[StrictBool] = Field(default=None, description="Specifies whether we can serve the GET request from the read replica cache. There is a lag of 15 seconds between the read replica and primary data source.", alias="useCachedData")
    cassandra_params: Optional[CassandraOnPremSearchParams] = Field(default=None, alias="cassandraParams")
    couchbase_params: Optional[CouchBaseOnPremSearchParams] = Field(default=None, alias="couchbaseParams")
    email_params: Optional[SearchEmailRequestParams] = Field(default=None, alias="emailParams")
    exchange_params: Optional[SearchExchangeObjectsRequestParams] = Field(default=None, alias="exchangeParams")
    file_params: Optional[SearchFileRequestParams] = Field(default=None, alias="fileParams")
    hbase_params: Optional[HbaseOnPremSearchParams] = Field(default=None, alias="hbaseParams")
    hdfs_params: Optional[HDFSOnPremSearchParams] = Field(default=None, alias="hdfsParams")
    hive_params: Optional[HiveOnPremSearchParams] = Field(default=None, alias="hiveParams")
    mongodb_params: Optional[MongoDbOnPremSearchParams] = Field(default=None, alias="mongodbParams")
    ms_groups_params: Optional[SearchMsGroupsRequestParams] = Field(default=None, alias="msGroupsParams")
    ms_teams_params: Optional[SearchMsTeamsRequestParams] = Field(default=None, alias="msTeamsParams")
    one_drive_params: Optional[SearchDocumentLibraryRequestParams] = Field(default=None, alias="oneDriveParams")
    public_folder_params: Optional[SearchPublicFolderRequestParams] = Field(default=None, alias="publicFolderParams")
    sfdc_params: Optional[SearchSfdcRecordsRequestParams] = Field(default=None, alias="sfdcParams")
    sharepoint_params: Optional[SearchDocumentLibraryRequestParams] = Field(default=None, alias="sharepointParams")
    uda_params: Optional[UdaOnPremSearchParams] = Field(default=None, alias="udaParams")
    __properties: ClassVar[List[str]] = ["count", "includeTenants", "mightHaveSnapshotTagIds", "mightHaveTagIds", "mustHaveSnapshotTagIds", "mustHaveTagIds", "objectType", "paginationCookie", "protectionGroupIds", "snapshotTags", "storageDomainIds", "tags", "tenantId", "useCachedData", "cassandraParams", "couchbaseParams", "emailParams", "exchangeParams", "fileParams", "hbaseParams", "hdfsParams", "hiveParams", "mongodbParams", "msGroupsParams", "msTeamsParams", "oneDriveParams", "publicFolderParams", "sfdcParams", "sharepointParams", "udaParams"]

    @field_validator('object_type')
    def object_type_validate_enum(cls, value):
        """Validates the enum"""
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
        """Create an instance of SearchIndexedObjectsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of one_drive_params
        if self.one_drive_params:
            _dict['oneDriveParams'] = self.one_drive_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of public_folder_params
        if self.public_folder_params:
            _dict['publicFolderParams'] = self.public_folder_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sfdc_params
        if self.sfdc_params:
            _dict['sfdcParams'] = self.sfdc_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sharepoint_params
        if self.sharepoint_params:
            _dict['sharepointParams'] = self.sharepoint_params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of uda_params
        if self.uda_params:
            _dict['udaParams'] = self.uda_params.to_dict()
        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if include_tenants (nullable) is None
        # and model_fields_set contains the field
        if self.include_tenants is None and "include_tenants" in self.model_fields_set:
            _dict['includeTenants'] = None

        # set to None if might_have_snapshot_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.might_have_snapshot_tag_ids is None and "might_have_snapshot_tag_ids" in self.model_fields_set:
            _dict['mightHaveSnapshotTagIds'] = None

        # set to None if might_have_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.might_have_tag_ids is None and "might_have_tag_ids" in self.model_fields_set:
            _dict['mightHaveTagIds'] = None

        # set to None if must_have_snapshot_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.must_have_snapshot_tag_ids is None and "must_have_snapshot_tag_ids" in self.model_fields_set:
            _dict['mustHaveSnapshotTagIds'] = None

        # set to None if must_have_tag_ids (nullable) is None
        # and model_fields_set contains the field
        if self.must_have_tag_ids is None and "must_have_tag_ids" in self.model_fields_set:
            _dict['mustHaveTagIds'] = None

        # set to None if pagination_cookie (nullable) is None
        # and model_fields_set contains the field
        if self.pagination_cookie is None and "pagination_cookie" in self.model_fields_set:
            _dict['paginationCookie'] = None

        # set to None if protection_group_ids (nullable) is None
        # and model_fields_set contains the field
        if self.protection_group_ids is None and "protection_group_ids" in self.model_fields_set:
            _dict['protectionGroupIds'] = None

        # set to None if storage_domain_ids (nullable) is None
        # and model_fields_set contains the field
        if self.storage_domain_ids is None and "storage_domain_ids" in self.model_fields_set:
            _dict['storageDomainIds'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if tenant_id (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_id is None and "tenant_id" in self.model_fields_set:
            _dict['tenantId'] = None

        # set to None if use_cached_data (nullable) is None
        # and model_fields_set contains the field
        if self.use_cached_data is None and "use_cached_data" in self.model_fields_set:
            _dict['useCachedData'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchIndexedObjectsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "includeTenants": obj.get("includeTenants") if obj.get("includeTenants") is not None else False,
            "mightHaveSnapshotTagIds": obj.get("mightHaveSnapshotTagIds"),
            "mightHaveTagIds": obj.get("mightHaveTagIds"),
            "mustHaveSnapshotTagIds": obj.get("mustHaveSnapshotTagIds"),
            "mustHaveTagIds": obj.get("mustHaveTagIds"),
            "objectType": obj.get("objectType"),
            "paginationCookie": obj.get("paginationCookie"),
            "protectionGroupIds": obj.get("protectionGroupIds"),
            "snapshotTags": obj.get("snapshotTags"),
            "storageDomainIds": obj.get("storageDomainIds"),
            "tags": obj.get("tags"),
            "tenantId": obj.get("tenantId"),
            "useCachedData": obj.get("useCachedData"),
            "cassandraParams": CassandraOnPremSearchParams.from_dict(obj["cassandraParams"]) if obj.get("cassandraParams") is not None else None,
            "couchbaseParams": CouchBaseOnPremSearchParams.from_dict(obj["couchbaseParams"]) if obj.get("couchbaseParams") is not None else None,
            "emailParams": SearchEmailRequestParams.from_dict(obj["emailParams"]) if obj.get("emailParams") is not None else None,
            "exchangeParams": SearchExchangeObjectsRequestParams.from_dict(obj["exchangeParams"]) if obj.get("exchangeParams") is not None else None,
            "fileParams": SearchFileRequestParams.from_dict(obj["fileParams"]) if obj.get("fileParams") is not None else None,
            "hbaseParams": HbaseOnPremSearchParams.from_dict(obj["hbaseParams"]) if obj.get("hbaseParams") is not None else None,
            "hdfsParams": HDFSOnPremSearchParams.from_dict(obj["hdfsParams"]) if obj.get("hdfsParams") is not None else None,
            "hiveParams": HiveOnPremSearchParams.from_dict(obj["hiveParams"]) if obj.get("hiveParams") is not None else None,
            "mongodbParams": MongoDbOnPremSearchParams.from_dict(obj["mongodbParams"]) if obj.get("mongodbParams") is not None else None,
            "msGroupsParams": SearchMsGroupsRequestParams.from_dict(obj["msGroupsParams"]) if obj.get("msGroupsParams") is not None else None,
            "msTeamsParams": SearchMsTeamsRequestParams.from_dict(obj["msTeamsParams"]) if obj.get("msTeamsParams") is not None else None,
            "oneDriveParams": SearchDocumentLibraryRequestParams.from_dict(obj["oneDriveParams"]) if obj.get("oneDriveParams") is not None else None,
            "publicFolderParams": SearchPublicFolderRequestParams.from_dict(obj["publicFolderParams"]) if obj.get("publicFolderParams") is not None else None,
            "sfdcParams": SearchSfdcRecordsRequestParams.from_dict(obj["sfdcParams"]) if obj.get("sfdcParams") is not None else None,
            "sharepointParams": SearchDocumentLibraryRequestParams.from_dict(obj["sharepointParams"]) if obj.get("sharepointParams") is not None else None,
            "udaParams": UdaOnPremSearchParams.from_dict(obj["udaParams"]) if obj.get("udaParams") is not None else None
        })
        return _obj


