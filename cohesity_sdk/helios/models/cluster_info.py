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
from cohesity_sdk.helios.models.available_release_version import AvailableReleaseVersion
from typing import Set
from typing_extensions import Self

class ClusterInfo(BaseModel):
    """
    Specifies the clusters hardware type, memory used and total memory capacity, health, connected or not, current version, available versions and the upgrade status.
    """ # noqa: E501
    available_versions: Optional[List[AvailableReleaseVersion]] = Field(default=None, description="Specifies the release versions the cluster can upgrade to.", alias="availableVersions")
    cluster_id: Optional[StrictInt] = Field(default=None, description="Specifies cluster id.", alias="clusterId")
    cluster_incarnation_id: Optional[StrictInt] = Field(default=None, description="Specifies cluster incarnation id.", alias="clusterIncarnationId")
    cluster_name: Optional[StrictStr] = Field(default=None, description="Specifies cluster's name.", alias="clusterName")
    current_version: Optional[StrictStr] = Field(default=None, description="Specifies if the cluster is connected to helios.", alias="currentVersion")
    health: Optional[StrictStr] = Field(default=None, description="Specifies the health of the cluster.")
    is_connected_to_helios: Optional[StrictBool] = Field(default=None, description="Specifies if the cluster is connected to helios.", alias="isConnectedToHelios")
    location: Optional[StrictStr] = Field(default=None, description="Specifies the location of the cluster.")
    node_ips: Optional[List[StrictStr]] = Field(default=None, description="Specifies an array of node ips for the cluster.", alias="nodeIps")
    number_of_nodes: Optional[StrictInt] = Field(default=None, description="Specifies the number of nodes in the cluster.", alias="numberOfNodes")
    provider_type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the cluster provider.", alias="providerType")
    scheduled_timestamp: Optional[StrictInt] = Field(default=None, description="Time at which an upgrade is scheduled.", alias="scheduledTimestamp")
    status: Optional[StrictStr] = Field(default=None, description="Specifies the upgrade status of the cluster.")
    target_version: Optional[StrictStr] = Field(default=None, description="Specifies target version to which clusters are to be upgraded.", alias="targetVersion")
    total_capacity: Optional[StrictInt] = Field(default=None, description="Specifies how total memory capacity of the cluster.", alias="totalCapacity")
    type: Optional[StrictStr] = Field(default=None, description="Specifies the type of the cluster.")
    used_capacity: Optional[StrictInt] = Field(default=None, description="Specifies how much of the cluster capacity is consumed.", alias="usedCapacity")
    __properties: ClassVar[List[str]] = ["availableVersions", "clusterId", "clusterIncarnationId", "clusterName", "currentVersion", "health", "isConnectedToHelios", "location", "nodeIps", "numberOfNodes", "providerType", "scheduledTimestamp", "status", "targetVersion", "totalCapacity", "type", "usedCapacity"]

    @field_validator('health')
    def health_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Critical', 'NonCritical']):
            raise ValueError("must be one of enum values ('Critical', 'NonCritical')")
        return value

    @field_validator('provider_type')
    def provider_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kMCMCohesity', 'kIBMStorageProtect']):
            raise ValueError("must be one of enum values ('kMCMCohesity', 'kIBMStorageProtect')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['InProgress', 'UpgradeAvailable', 'UpToDate', 'Scheduled', 'Failed', 'ClusterUnreachable']):
            raise ValueError("must be one of enum values ('InProgress', 'UpgradeAvailable', 'UpToDate', 'Scheduled', 'Failed', 'ClusterUnreachable')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['VMRobo', 'Physical']):
            raise ValueError("must be one of enum values ('VMRobo', 'Physical')")
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
        """Create an instance of ClusterInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available_versions (list)
        _items = []
        if self.available_versions:
            for _item_available_versions in self.available_versions:
                if _item_available_versions:
                    _items.append(_item_available_versions.to_dict())
            _dict['availableVersions'] = _items
        # set to None if available_versions (nullable) is None
        # and model_fields_set contains the field
        if self.available_versions is None and "available_versions" in self.model_fields_set:
            _dict['availableVersions'] = None

        # set to None if cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_id is None and "cluster_id" in self.model_fields_set:
            _dict['clusterId'] = None

        # set to None if cluster_incarnation_id (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_incarnation_id is None and "cluster_incarnation_id" in self.model_fields_set:
            _dict['clusterIncarnationId'] = None

        # set to None if cluster_name (nullable) is None
        # and model_fields_set contains the field
        if self.cluster_name is None and "cluster_name" in self.model_fields_set:
            _dict['clusterName'] = None

        # set to None if current_version (nullable) is None
        # and model_fields_set contains the field
        if self.current_version is None and "current_version" in self.model_fields_set:
            _dict['currentVersion'] = None

        # set to None if health (nullable) is None
        # and model_fields_set contains the field
        if self.health is None and "health" in self.model_fields_set:
            _dict['health'] = None

        # set to None if is_connected_to_helios (nullable) is None
        # and model_fields_set contains the field
        if self.is_connected_to_helios is None and "is_connected_to_helios" in self.model_fields_set:
            _dict['isConnectedToHelios'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if node_ips (nullable) is None
        # and model_fields_set contains the field
        if self.node_ips is None and "node_ips" in self.model_fields_set:
            _dict['nodeIps'] = None

        # set to None if number_of_nodes (nullable) is None
        # and model_fields_set contains the field
        if self.number_of_nodes is None and "number_of_nodes" in self.model_fields_set:
            _dict['numberOfNodes'] = None

        # set to None if provider_type (nullable) is None
        # and model_fields_set contains the field
        if self.provider_type is None and "provider_type" in self.model_fields_set:
            _dict['providerType'] = None

        # set to None if scheduled_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_timestamp is None and "scheduled_timestamp" in self.model_fields_set:
            _dict['scheduledTimestamp'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if target_version (nullable) is None
        # and model_fields_set contains the field
        if self.target_version is None and "target_version" in self.model_fields_set:
            _dict['targetVersion'] = None

        # set to None if total_capacity (nullable) is None
        # and model_fields_set contains the field
        if self.total_capacity is None and "total_capacity" in self.model_fields_set:
            _dict['totalCapacity'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if used_capacity (nullable) is None
        # and model_fields_set contains the field
        if self.used_capacity is None and "used_capacity" in self.model_fields_set:
            _dict['usedCapacity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ClusterInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "availableVersions": [AvailableReleaseVersion.from_dict(_item) for _item in obj["availableVersions"]] if obj.get("availableVersions") is not None else None,
            "clusterId": obj.get("clusterId"),
            "clusterIncarnationId": obj.get("clusterIncarnationId"),
            "clusterName": obj.get("clusterName"),
            "currentVersion": obj.get("currentVersion"),
            "health": obj.get("health"),
            "isConnectedToHelios": obj.get("isConnectedToHelios"),
            "location": obj.get("location"),
            "nodeIps": obj.get("nodeIps"),
            "numberOfNodes": obj.get("numberOfNodes"),
            "providerType": obj.get("providerType"),
            "scheduledTimestamp": obj.get("scheduledTimestamp"),
            "status": obj.get("status"),
            "targetVersion": obj.get("targetVersion"),
            "totalCapacity": obj.get("totalCapacity"),
            "type": obj.get("type"),
            "usedCapacity": obj.get("usedCapacity")
        })
        return _obj


