#    Copyright 2019, A10 Networks
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# ==============
# Argument Names
# ==============
LOADBALANCERS_LIST = 'loadbalancers_list'
VRID_LIST = 'vrid_list'
SET_THUNDER_UPDATE_AT = 'set-thunder-update-at'
SET_THUNDER_BACKUP_UPDATE_AT = 'set-thunder-backup-update-at'

# Member count with specific IP.
MEMBER_COUNT_IP = 'member_count_ip'
MEMBER_COUNT_IP_PORT_PROTOCOL = 'member_count_ip_port_protocol'
POOL_COUNT_IP = 'pool_count_ip'
WRITE_MEM_SHARED_PART = 'write_mem_shared_part'
WRITE_MEM_FOR_SHARED_PARTITION = 'write_memory_for_shared_partition'
WRITE_MEM_FOR_LOCAL_PARTITION = 'write_memory_for_local_partition'

MEMBER_LIST = 'member_list'
SUBNET_LIST = 'subnet_list'
MEMBERS = 'members'
POOLS = 'pools'

PARTITION_PROJECT_LIST = 'partition_project_list'
IFNUM_BACKUP = 'ifnum_backup'
IFNUM_MASTER = 'ifnum_master'
LISTENER_STATS = 'listener_stats'

# Octavia taskflow flow and task names (missing name in victoria octavia)
RELOADLOAD_BALANCER = 'octavia-reloadload-balancer'

VTHUNDER = 'vthunder'
STATUS = 'status'
ROLE = 'role'
BACKUP_VTHUNDER = 'backup_vthunder'
MASTER_VTHUNDER = 'master_vthunder'
VRRP_STATUS = 'vrrp_status'
MASTER_VRRP_STATUS = 'master_vrrp_status'
BACKUP_VRRP_STATUS = 'backup_vrrp_status'
NAT_POOL = 'nat_pool'
NAT_FLAVOR = 'nat_flavor'
SUBNET_PORT = 'subnet_port'
WRITE_MEM_SHARED = 'write_mem_shared'
WRITE_MEM_PRIVATE = 'write_mem_private'

FAILED = 'FAILED'
USED_SPARE = 'USED_SPARE'
SPARE_VTHUNDER = 'spare_vthunder'
FAILOVER_VTHUNDER = 'failover_vthunder'
OCTAVIA_HEALTH_MANAGER_CONTROLLER = 'octavia_health_manager_controller'
OCTAVIA_HEALTH_MONITOR = 'octavia_health_monitor'
VTHUNDER_CONFIG = 'vthunder_config'
DEVICE_CONFIG_DICT = 'device_config_dict'
DEVICE_KEY_PREFIX = '[dev]'
USE_DEVICE_FLAVOR = 'use_device_flavor'
VTHUNDER_ID = "vthunder_id"
DEVICE_ID = "device_id"
SET_ID = "set_id"
VRID = "vrid"
DEVICE_PRIORITY = 'device_priority'
FLOATING_IP = 'floating_ip'
FLOATING_IP_MASK = 'floating_ip_mask'
CERT_DATA = 'cert_data'
SP_OBJ_DICT = {
    'HTTP_COOKIE': "cookie_persistence",
    'APP_COOKIE': "cookie_persistence",
    'SOURCE_IP': "src_ip_persistence",
}
HTTP_TYPE = ['HTTP', 'HTTPS']
PERS_TYPE = ['cookie_persistence', 'src_ip_persistence']
NO_DEST_NAT_SUPPORTED_PROTOCOL = ['tcp', 'udp']
PORT = 'port'
LB_COUNT = 'lb_count'
LB_COUNT_SUBNET = 'lb_count_subnet'
LB_COUNT_FLAVOR = 'lb_count_flavor'
MEMBER_COUNT = 'member_count'
DELETE_VRID = 'delete_vrid'
LB_COUNT_THUNDER = 'lb_count_thunder'
MEMBER_COUNT_THUNDER = 'member_count_thunder'
LB_COUNT_THUNDER_PARTITION = 'lb_count_thunder_partition'

ID = 'id'
SECURITY_GROUPS = 'security_groups'
VIP_SEC_GROUP_PREFIX = 'lb-'
LB_RESOURCE = 'lb_resource'

SUBNET_ID = "subnet_id"
VLAN_ID = "vlan_id"
TAG_INTERFACE = "tag_interface"
VE_INTERFACE = "ve_interface"
DELETE_VLAN = "delete_vlan"
VLAN = "vlan"
FLAT = "flat"
SUPPORTED_NETWORK_TYPE = [FLAT, VLAN]
SSL_TEMPLATE = "ssl_template"

COMPUTE_BUSY = "compute_busy"
VTHUNDER_LIST = "vthunder_list"
NETWORK_LIST = "network_list"
ADDED_NETWORK = "added_network"

COMPUTE_PAUSED = "PAUSED"
L2DSR_FLAVOR = "l2dsr_flavor"
MASTER_AMPHORA_STATUS = "master_amphora_status"
BACKUP_AMPHORA_STATUS = "backup_amphora_status"

FLOW_TYPE = 'flow_type'
FLOW_TYPE_DELETE = 'delete'

# ACOS versions
ACOS_5_2_1_P2 = "5.2.1-P2"

# Proxy Protocol Object name
PROXY_POOL_COUNT = 'proxy_pool_count'
PROXY_PROTOCPL_TEMPLATE_NAME = 'octavia_proxy_protocol_v1'
PROXY_PROTOCPL_V2_TEMPLATE_NAME = 'octavia_proxy_protocol_v2'
PROXY_PROTOCPL_AFLEX_NAME = 'octavia_aflex_proxy_protocol_v1'
PROXY_PROTOCPL_V1 = "v1"
PROXY_PROTOCPL_V2 = "v2"


# ============================
# Taskflow flow and task names
# ============================
GET_VTHUNDER_FOR_LB_SUBFLOW = 'octavia-get-vthunder-for-lb-subflow'
BACKUP_AMPHORA_PLUG = 'backup-amphora-plug'
GET_MASTER_VTHUNDER_INTERFACE = 'get-master-vthunder-intercae'
GET_BACKUP_VTHUNDER_INTERFACE = 'get-backup-vthunder-intercae'
MASTER_CONNECTIVITY_WAIT = 'master-connectivity-wait'
BACKUP_CONNECTIVITY_WAIT = 'backup-connectivity-wait'
ENABLE_MASTER_VTHUNDER_INTERFACE = 'enable-master-vthunder-interface'
ENABLE_BACKUP_VTHUNDER_INTERFACE = 'enable-backup-vthunder-interface'
ENABLE_VTHUNDER_INTERFACE = 'enable-vthunder-interface'
MASTER_ENABLE_INTERFACE = 'master-enable-interface'
BACKUP_ENABLE_INTERFACE = 'backup-enable-interface'
MARK_VTHUNDER_MASTER_ACTIVE_IN_DB = 'mark-vthunder-master-active-in-db'
MARK_VTHUNDER_BACKUP_ACTIVE_IN_DB = 'mark-vthunder-backup-active-in-db'
MARK_VTHUNDER_MASTER_DELETED_IN_DB = 'mark-vthunder-master-deleted-in-db'
MARK_VTHUNDER_BACKUP_DELETED_IN_DB = 'mark-vthunder-backup-deleted-in-db'
GET_BACKUP_VTHUNDER_BY_LB = 'get-backup-vthunder-by-lb'
GET_VTHUNDER_FROM_LB = 'get-vthunder-from-lb'
CREATE_HEALTH_MONITOR_ON_VTHUNDER = 'create-health-monitor-on-vthunder'
CREATE_HEALTH_MONITOR_ON_SPARE = 'create-health-monitor-on-spare'
MARK_AMPHORA_READY_INDB = 'mark-amphora-ready-indb'
HANDLE_SESS_PERS = 'handle-session-persistence-delta-subflow'
GET_LOADBALANCER_FROM_DB = 'Get-Loadbalancer-from-db'
GET_BACKUP_LOADBALANCER_FROM_DB = 'get-backup-loadbalancer-from-db'
CONFIGURE_VRRP_FOR_MASTER_VTHUNDER = 'configure-vrrp-for-master-vthunder'
CONFIGURE_VRRP_FOR_BACKUP_VTHUNDER = 'configure-vrrp-for-backup-vthunder'
CONFIGURE_VRID_FOR_MASTER_VTHUNDER = 'configure-vrid-for-master-vthunder'
CONFIGURE_VRID_FOR_BACKUP_VTHUNDER = 'configure-vrid-for-backup-vthunder'
WAIT_FOR_MASTER_SYNC = 'wait-for-master-sync'
WAIT_FOR_BACKUP_SYNC = 'wait-for-backup-sync'
CONFIGURE_AVCS_SYNC_FOR_MASTER = 'configure-avcs-sync-for-master'
CONFIGURE_AVCS_SYNC_FOR_BACKUP = 'configure-avcs-sync-for-backup'
CONFIGURE_AVCS_FOR_FAILOVER = 'configure-avcs-for-failover'
CHECK_VRRP_STATUS = 'check-vrrp-status'
CHECK_VRRP_MASTER_STATUS = 'check-vrrp-master-status'
CHECK_VRRP_BACKUP_STATUS = 'check-vrrp-backup-status'
CONFIRM_VRRP_STATUS = 'confirm-vrrp-status'
ADD_VRRP_SET_ID_INDB = 'add-vrrp-set-id-db'
DELETE_VRRP_SET_ID_INDB = 'delete-vrrp-set-id-db'
GET_VRRP_SET_ID_INDB = 'get-vrrp-set-id-db'
ALLOCATE_VIP = 'allocate-vip'
UPDATE_VIP_AFTER_ALLOCATION = 'update-vip-after-allocation'
ALLOW_L2DSR = 'allow-l2dsr'
ALLOW_NO_SNAT = 'allow-no-snat'
AMPHORAE_POST_VIP_PLUG = 'amphorae-post-vip-plug'
AMPHORA_POST_NETWORK_UNPLUG = 'amphorae-post-network-plug'
AMPHORA_POST_NETWORK_UNPLUG_FOR_BACKUP_VTHUNDER = 'amphorae-post-network-plug-for-backup-vthunder'
AMP_POST_VIP_PLUG = 'amp-post-vip-plug'
AMPHORAE_POST_VIP_PLUG_FOR_MASTER = 'amphorae-post-vip-plug-for-master'
AMPHORAE_POST_VIP_PLUG_FOR_BACKUP = 'amphorae-post-vip-plug-for-backup'
VCS_RELOAD = 'vcs-reload'
GET_BACKUP_VTHUNDER = 'get-backup-vthunder'
GET_MASTER_VTHUNDER = 'get-master-vthunder'
CONNECTIVITY_WAIT_FOR_MASTER_VTHUNDER = 'connectivity-wait-for-master-vthunder'
CONNECTIVITY_WAIT_FOR_BACKUP_VTHUNDER = 'connectivity-wait-for-backup-vthunder'
GET_VTHUNDER_MASTER = 'get-vthunder-master'
WAIT_FOR_MASTER_VCS_RELOAD = 'wait-for-master-vcs-reload'
WAIT_FOR_BACKUP_VCS_RELOAD = 'wait-for-backup-vcs-reload'
VCS_SYNC_WAIT = "wait-for-vcs_ready"
GET_COMPUTE_FOR_PROJECT = 'get-compute-for-project'
VALIDATE_COMPUTE_FOR_PROJECT = 'validate-compute-for-project'
GET_SPARE_COMPUTE_FOR_PROJECT = 'get-spare-compute-for-project'
DELETE_STALE_SPARE_VTHUNDER = 'delete-stale-spare-vthunder'
CREATE_VTHUNDER_ENTRY = 'create-vthunder-entry'
UPDATE_ACOS_VERSION_IN_VTHUNDER_ENTRY = 'update-acos-version-in-vthunder-entry'
UPDATE_ACOS_VERSION_FOR_BACKUP_VTHUNDER = 'update-acos-version-for-backup-vthunder'
VTHUNDER_BY_LB = 'vthunder-by-loadbalancer'
GET_VTHUNDER_BY_LB = 'get-vthunder-by-lb'
VTHUNDER_CONNECTIVITY_WAIT = 'vthunder-connectivity-wait'
WAIT_FOR_VTHUNDER_CONNECTIVITY = 'wait-for-vthunder-connectivity'
CHANGE_PARTITION = 'change-partition'
CREATE_SSL_CERT_FLOW = 'create-ssl-cert-flow'
DELETE_SSL_CERT_FLOW = 'delete-ssl-cert-flow'
UPDATE_SSL_CERT_FLOW = 'update-ssl-cert-flow'
LISTENER_TYPE_DECIDER_FLOW = 'listener_type_decider_flow'
DELETE_LOADBALANCER_VRID_SUBFLOW = 'delete-loadbalancer-vrid-subflow'
REVOKE_ACTIVE_VTHUNDER_LICENSE = 'revoke-active-vthunder-license'
REVOKE_BACKUP_VTHUNDER_LICENSE = 'revoke-backup-vthunder-license'
HANDLE_VRID_LOADBALANCER_SUBFLOW = 'handle-vrid-loadbalancer-subflow'
CREATE_MEMBER_SNAT_POOL_SUBFLOW = 'create-member-snat-pool-subflow'
DELETE_MEMBER_VTHUNDER_INTERNAL_SUBFLOW = 'delete-member-vthunder-internal-subflow'
DELETE_MEMBER_VRID_SUBFLOW = 'delete-member-vrid-subflow'
DELETE_MEMBER_VRID_INTERNAL_SUBFLOW = 'delete-member-vrid-internal-subflow'
DELETE_HEALTH_MONITOR_VTHUNDER_SUBFLOW = 'delete-hm-vthunder-subflow'
DELETE_HEALTH_MONITOR_SUBFLOW_WITH_POOL_DELETE_FLOW = 'delete-health-monitor-subflow' \
                                                      '-with-pool-delete-flow'
DELETE_MEMBERS_SUBFLOW_WITH_POOL_DELETE_FLOW = 'delete-members-subflow-with-pool-delete-flow'
HANDLE_VRID_MEMBER_SUBFLOW = 'handle-vrid-member-subflow'
SPARE_VTHUNDER_CREATE = 'spare-vthunder-create'
ACTIVATE_GLM_LICENSE_SUBFLOW = 'activate-glm-license-subflow'
CONFIGURE_DNS_NAMESERVERS = 'configure-dns-nameservers'

ACTIVATE_FLEXPOOL_LICENSE = 'activate-flexpool-license'
CONFIGURE_PROXY_SERVER = 'configure-proxy-server'
SET_VTHUNDER_HOSTNAME = 'set-vthunder-hostname'
WRITE_MEMORY_THUNDER_FLOW = 'write-memory-thunder-flow'
RELOAD_CHECK_THUNDER_FLOW = 'reload-check-thunder-flow'
LB_TO_VTHUNDER_SUBFLOW = 'lb-to-vthunder-subflow'
GET_SPARE_AMPHORA_SBUFLOW = 'get-sapre_amphora-subflow'
GET_LB_RESOURCE = 'get-lb-resource'
GET_LB_RESOURCE_SUBNET = 'get-lb-resource-subnet'
GET_PROJECT_COUNT = 'get-child-parent-project-count'
GET_LB_COUNT_SUBNET = 'get-lb-count-by-subnet'
UPDATE_LISTENER_STATS_FLOW = 'update-listener-stats-flow'
GET_VTHUNDER_AMPHORA = 'get-vthunder-amphora'
COMPUTE_DELETE = 'compute-delete'
SET_VTHUNDER_TO_STANDBY = 'set-vthunder-to-standby'
GET_LBS_BY_THUNDER = 'get-loadbalancers-by-thunder'
MARK_LB_PENIND_UPDATE_IN_DB = 'mark-vthunder-pending-update-in-db'
MARK_LB_ACTIVE_IN_DB = 'mark-vthunder-active-in-db'
GET_VTHUNDER_NETWORK_LIST = 'get-vthunder-network-list'
GET_AMPHORA_FOR_FAILOVER = 'get-amphora-for-failover'
PLUG_NETWORK_BY_IDS = 'plug-network-by-ids'
PLUG_VIP_NETWORK_ON_SPARE = 'plusg-vip-network-on-spare'
POST_SPARE_PLUG_NETWORK = 'post-failover-plug-network'
GET_VCS_DEVICE_ID = 'get-vcs-device-id'
POST_FAILOVER_DB_UPDATE = 'post-failover-db-update'
MARK_LB_LIST_ERROR_ON_REVERT = 'mark-lb-list-error-on-revert'

FULLY_POPULATED_LISTENER_CREATE = 'fully-populated-listener-create'
FULLY_POPULATED_ERROR_ON_REVERT = '-error-on-revert'
FULLY_POPULATED_GET_FLAVOR = '-get-flavor'
FULLY_POPULATED_NAT_CREATE = '-natpool-create'
FULLY_POPULATED_CREATE_LISTENER = '-create-listener'
FULLY_POPULATED_MARK_LISTENER_ACTIVE = '-mark-listener-active'
FULLY_POPULATED_GET_POOL_LISTENER = '-get-pool-listener'
FULLY_POPULATED_CREATE_POOL = '-create-pool'
FULLY_POPULATED_MARK_POOL_ACTIVE = '-mark-pool-active'
FULLY_POPULATED_VALID_SUBNET = '-validate-subnet'
FULLY_POPULATED_CREATE_MEMBER = '-create-member'
FULLY_POPULATED_MARK_MEMBER_ACTIVE = '-mark-member-active'
FULLY_POPULATED_CREATE_HM = '-create-hm'
FULLY_POPULATED_MARK_HM_ACTIVE = '-mark-hm-active'
FULLY_POPULATED_CREATE_L7POLICY = '-create-l7policy'
FULLY_POPULATED_MARK_L7POLICY_ACTIVE = '-mark-l7policy-active'
FULLY_POPULATED_CREATE_L7RULE = '-create-l7rule'
FULLY_POPULATED_MARK_L7RULE_ACTIVE = '-mark-l7rule-active'

# ======================
# Non-Taskflow Constants
# ======================

OCTAVIA_OWNER = 'Octavia'
TOPOLOGY_SPARE = 'SPARE'
READY = "READY"
