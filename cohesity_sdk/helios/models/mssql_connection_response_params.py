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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from cohesity_sdk.helios.models.aag_group import AAGGroup
from cohesity_sdk.helios.models.error import Error
from cohesity_sdk.helios.models.fci_cluster import FCICluster
from cohesity_sdk.helios.models.sql_server import SQLServer
from typing import Set
from typing_extensions import Self

class MssqlConnectionResponseParams(BaseModel):
    """
    Specifies the response parameters after connecting to a SQL node/cluster using given IP or hostname FQDN.
    """ # noqa: E501
    host_identifier: StrictStr = Field(description="Specifies the unique identifier to locate the SQL node or cluster. The host identifier can be IP address or FQDN.", alias="hostIdentifier")
    aag_groups: Optional[List[AAGGroup]] = Field(default=None, description="Specifies the list of AAG (Always on Avalibility) groups.", alias="aagGroups")
    error: Optional[Error] = None
    fci_clusters: Optional[List[FCICluster]] = Field(default=None, description="Specifies the list of FCI (Failover Cluster Instaces) Clusters. This will contain the list of all failover pools under a windows cluster. FCI clusters which are part of AAG, will be returned seperatly under aagServers field.", alias="fciClusters")
    servers: Optional[List[SQLServer]] = Field(default=None, description="Specifies the list of SQL servers. If SQL server is a part of avalibility group then it will be returned in aagServers field. This will include the list of all standalone SQL servers and servers belonging to any FCI enviournment.")
    skip_connection_discovery: Optional[StrictBool] = Field(default=None, description="Specifies whether to skip the discovery phase of all SQL servers, AAG groups etc during registration process.", alias="skipConnectionDiscovery")
    __properties: ClassVar[List[str]] = ["hostIdentifier", "aagGroups", "error", "fciClusters", "servers", "skipConnectionDiscovery"]

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
        """Create an instance of MssqlConnectionResponseParams from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in aag_groups (list)
        _items = []
        if self.aag_groups:
            for _item_aag_groups in self.aag_groups:
                if _item_aag_groups:
                    _items.append(_item_aag_groups.to_dict())
            _dict['aagGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fci_clusters (list)
        _items = []
        if self.fci_clusters:
            for _item_fci_clusters in self.fci_clusters:
                if _item_fci_clusters:
                    _items.append(_item_fci_clusters.to_dict())
            _dict['fciClusters'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in servers (list)
        _items = []
        if self.servers:
            for _item_servers in self.servers:
                if _item_servers:
                    _items.append(_item_servers.to_dict())
            _dict['servers'] = _items
        # set to None if aag_groups (nullable) is None
        # and model_fields_set contains the field
        if self.aag_groups is None and "aag_groups" in self.model_fields_set:
            _dict['aagGroups'] = None

        # set to None if fci_clusters (nullable) is None
        # and model_fields_set contains the field
        if self.fci_clusters is None and "fci_clusters" in self.model_fields_set:
            _dict['fciClusters'] = None

        # set to None if servers (nullable) is None
        # and model_fields_set contains the field
        if self.servers is None and "servers" in self.model_fields_set:
            _dict['servers'] = None

        # set to None if skip_connection_discovery (nullable) is None
        # and model_fields_set contains the field
        if self.skip_connection_discovery is None and "skip_connection_discovery" in self.model_fields_set:
            _dict['skipConnectionDiscovery'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MssqlConnectionResponseParams from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostIdentifier": obj.get("hostIdentifier"),
            "aagGroups": [AAGGroup.from_dict(_item) for _item in obj["aagGroups"]] if obj.get("aagGroups") is not None else None,
            "error": Error.from_dict(obj["error"]) if obj.get("error") is not None else None,
            "fciClusters": [FCICluster.from_dict(_item) for _item in obj["fciClusters"]] if obj.get("fciClusters") is not None else None,
            "servers": [SQLServer.from_dict(_item) for _item in obj["servers"]] if obj.get("servers") is not None else None,
            "skipConnectionDiscovery": obj.get("skipConnectionDiscovery")
        })
        return _obj


