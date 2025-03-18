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
from typing import Set
from typing_extensions import Self

class CommonSearchIndexedObjectsRequestParams(BaseModel):
    """
    Specifies the common params to search for indexed objects.
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
    __properties: ClassVar[List[str]] = ["count", "includeTenants", "mightHaveSnapshotTagIds", "mightHaveTagIds", "mustHaveSnapshotTagIds", "mustHaveTagIds", "objectType", "paginationCookie", "protectionGroupIds", "snapshotTags", "storageDomainIds", "tags", "tenantId", "useCachedData"]

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
        """Create an instance of CommonSearchIndexedObjectsRequestParams from a JSON string"""
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
        """Create an instance of CommonSearchIndexedObjectsRequestParams from a dict"""
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
            "useCachedData": obj.get("useCachedData")
        })
        return _obj


