Search.setIndex({envversion:47,filenames:["index","introduction/index","introduction/native","introduction/quickstart","license","reference/api/gssa","reference/api/gssa.comparator","reference/api/gssa.families","reference/api/modules","reference/cdm/algorithms","reference/cdm/contexts","reference/cdm/index","reference/cdm/parameters","reference/comparison","reference/docker/container-module","reference/docker/fenics","reference/docker/index","reference/docs","reference/errors","reference/families","reference/gssa-xml","reference/index","reference/server/database","reference/server/executables","reference/server/index","reference/server/router","reference/server/transferrers"],objects:{"":{gssa:[5,0,0,"-"]},"gssa.client":{GoSmartSimulationClientComponent:[5,3,1,""],wrapped_coroutine:[5,4,1,""]},"gssa.client.GoSmartSimulationClientComponent":{finalize:[5,2,1,""],make_call:[5,2,1,""],onComplete:[5,2,1,""],onFail:[5,2,1,""],onJoin:[5,2,1,""],onLeave:[5,2,1,""],onStatus:[5,2,1,""],shutdown:[5,2,1,""]},"gssa.comparator":{comparator:[6,0,0,"-"],parse:[6,0,0,"-"],simulation_definition:[6,0,0,"-"]},"gssa.comparator.comparator":{Comparator:[6,3,1,""]},"gssa.comparator.comparator.Comparator":{diff:[6,2,1,""],equal:[6,2,1,""],left_text:[6,1,1,""],right_text:[6,1,1,""]},"gssa.comparator.parse":{gssa_xml_to_definition:[6,4,1,""]},"gssa.comparator.simulation_definition":{SimulationDefinition:[6,3,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition":{Algorithm:[6,3,1,""],Argument:[6,3,1,""],Needle:[6,3,1,""],NumericalModel:[6,3,1,""],Parameter:[6,3,1,""],Region:[6,3,1,""],Transferrer:[6,3,1,""],add_algorithm:[6,2,1,""],add_parameter:[6,2,1,""],algorithms:[6,1,1,""],diff:[6,2,1,""],name:[6,1,1,""],numerical_model:[6,1,1,""],parameters:[6,1,1,""],set_numerical_model:[6,2,1,""],set_transferrer:[6,2,1,""],transferrer:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Algorithm":{arguments:[6,1,1,""],content:[6,1,1,""],diff:[6,2,1,""],result:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Argument":{diff:[6,2,1,""],name:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Needle":{cls:[6,1,1,""],diff:[6,2,1,""],file:[6,1,1,""],index:[6,1,1,""],parameters:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.NumericalModel":{definition:[6,1,1,""],diff:[6,2,1,""],needles:[6,1,1,""],regions:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Parameter":{diff:[6,2,1,""],name:[6,1,1,""],typ:[6,1,1,""],value:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Region":{diff:[6,2,1,""],format:[6,1,1,""],groups:[6,1,1,""],id:[6,1,1,""],input:[6,1,1,""],name:[6,1,1,""]},"gssa.comparator.simulation_definition.SimulationDefinition.Transferrer":{cls:[6,1,1,""],diff:[6,2,1,""],url:[6,1,1,""]},"gssa.config":{get:[5,4,1,""],get_api_version:[5,4,1,""],get_config_file:[5,4,1,""],init_config:[5,4,1,""],init_logger:[5,4,1,""]},"gssa.database":{SQLiteSimulationDatabase:[5,3,1,""]},"gssa.database.SQLiteSimulationDatabase":{"delete":[5,2,1,""],active_count:[5,2,1,""],addOrUpdate:[5,2,1,""],all:[5,2,1,""],create:[5,2,1,""],getStatusAndValidation:[5,2,1,""],getValidation:[5,2,1,""],markAllOld:[5,2,1,""],retrieve:[5,2,1,""],search:[5,2,1,""],setStatus:[5,2,1,""],updateValidation:[5,2,1,""]},"gssa.definition":{GoSmartSimulationDefinition:[5,3,1,""]},"gssa.definition.GoSmartSimulationDefinition":{cancel:[5,2,1,""],clean:[5,2,1,""],create_xml_from_string:[5,2,1,""],finalize:[5,2,1,""],finalized:[5,2,1,""],gather_diagnostic:[5,2,1,""],gather_results:[5,2,1,""],get_dir:[5,2,1,""],get_exit_status:[5,2,1,""],get_files:[5,2,1,""],get_guid:[5,2,1,""],get_remote_dir:[5,2,1,""],init_percentage_socket_server:[5,2,1,""],push_files:[5,2,1,""],set_exit_status:[5,2,1,""],set_remote_dir:[5,2,1,""],simulate:[5,2,1,""],summary:[5,2,1,""],update_files:[5,2,1,""],validation:[5,2,1,""]},"gssa.docker":{OutputHandler:[5,3,1,""],Submitter:[5,3,1,""]},"gssa.docker.OutputHandler":{on_moved:[5,2,1,""]},"gssa.docker.Submitter":{add_input:[5,2,1,""],cancel:[5,2,1,""],copy_output:[5,2,1,""],destroy:[5,2,1,""],finalize:[5,2,1,""],notify_output:[5,2,1,""],output:[5,2,1,""],reader:[5,1,1,""],receive_response:[5,2,1,""],run_script:[5,2,1,""],send_command:[5,2,1,""],set_update_socket:[5,2,1,""],writer:[5,1,1,""]},"gssa.error":{Error:[5,3,1,""],ErrorException:[5,5,1,""],ErrorMessage:[5,3,1,""],makeError:[5,4,1,""]},"gssa.error.ErrorException":{get_error:[5,2,1,""]},"gssa.families":{docker:[7,0,0,"-"],elmer_libnuma:[7,0,0,"-"],elmer_libnuma_legacy:[7,0,0,"-"],fenics:[7,0,0,"-"],g:[7,0,0,"-"],gssf_arguments:[7,0,0,"-"],mesher_gssf:[7,0,0,"-"],scan:[7,4,1,""]},"gssa.families.docker":{DockerFamily:[7,3,1,""]},"gssa.families.docker.DockerFamily":{cancel:[7,2,1,""],clean:[7,2,1,""],get_needle_parameter:[7,2,1,""],get_parameter:[7,2,1,""],get_percentage_socket_location:[7,2,1,""],load_definition:[7,2,1,""],prepare_simulation:[7,2,1,""],retrieve_files:[7,2,1,""],simulate:[7,2,1,""]},"gssa.families.elmer_libnuma":{ElmerLibNumaFamily:[7,3,1,""]},"gssa.families.elmer_libnuma.ElmerLibNumaFamily":{clean:[7,2,1,""],family_name:[7,1,1,""],get_needle_parameter:[7,2,1,""],get_parameter:[7,2,1,""],get_percentage_socket_location:[7,2,1,""],load_definition:[7,2,1,""],prepare_simulation:[7,2,1,""],retrieve_files:[7,2,1,""],to_xml:[7,2,1,""],validation:[7,2,1,""]},"gssa.families.elmer_libnuma_legacy":{ElmerLibNumaLegacyFamily:[7,3,1,""]},"gssa.families.elmer_libnuma_legacy.ElmerLibNumaLegacyFamily":{clean:[7,2,1,""],family_name:[7,1,1,""],get_needle_parameter:[7,2,1,""],get_parameter:[7,2,1,""],get_percentage_socket_location:[7,2,1,""],load_definition:[7,2,1,""],retrieve_files:[7,2,1,""],simulate:[7,2,1,""],to_xml:[7,2,1,""],validation:[7,2,1,""]},"gssa.families.fenics":{FenicsFamily:[7,3,1,""]},"gssa.families.fenics.FenicsFamily":{family_name:[7,1,1,""],prepare_simulation:[7,2,1,""]},"gssa.families.g":{GFoamFamily:[7,3,1,""]},"gssa.families.g.GFoamFamily":{family_name:[7,1,1,""]},"gssa.families.gssf_arguments":{GoSmartSimulationFrameworkArguments:[7,3,1,""]},"gssa.families.gssf_arguments.GoSmartSimulationFrameworkArguments":{to_list:[7,2,1,""]},"gssa.families.mesher_gssf":{MesherGSSFMixin:[7,3,1,""]},"gssa.families.mesher_gssf.MesherGSSFMixin":{init_mesher:[7,2,1,""],mesh:[7,2,1,""],to_mesh_xml:[7,2,1,""]},"gssa.family":{Family:[5,3,1,""],FamilyType:[5,3,1,""]},"gssa.family.Family":{cancel:[5,2,1,""],family_name:[5,1,1,""],get_needle_parameter:[5,2,1,""],get_parameter:[5,2,1,""],load_core_definition:[5,2,1,""],validation:[5,2,1,""]},"gssa.http_transferrer":{HTTPTransferrer:[5,3,1,""]},"gssa.http_transferrer.HTTPTransferrer":{configure_from_xml:[5,2,1,""],connect:[5,2,1,""],disconnect:[5,2,1,""],downloadFile:[5,2,1,""],pull_files:[5,2,1,""],push_files:[5,2,1,""],uploadFile:[5,2,1,""]},"gssa.parameters":{convert_parameter:[5,4,1,""],read_parameters:[5,4,1,""]},"gssa.server":{GoSmartSimulationServerComponent:[5,3,1,""]},"gssa.server.GoSmartSimulationServerComponent":{client:[5,1,1,""],current:[5,1,1,""],doApi:[5,2,1,""],doCancel:[5,2,1,""],doClean:[5,2,1,""],doCompare:[5,2,1,""],doFinalize:[5,2,1,""],doInit:[5,2,1,""],doProperties:[5,2,1,""],doRequestDiagnostic:[5,2,1,""],doRequestFiles:[5,2,1,""],doRequestResults:[5,2,1,""],doRetrieveStatus:[5,2,1,""],doSearch:[5,2,1,""],doSimulate:[5,2,1,""],doStart:[5,2,1,""],doTmpValidation:[5,2,1,""],doUpdateFiles:[5,2,1,""],doUpdateSettingsXml:[5,2,1,""],eventComplete:[5,2,1,""],eventFail:[5,2,1,""],getProperties:[5,2,1,""],onRequestAnnounce:[5,2,1,""],onRequestIdentify:[5,2,1,""],setDatabase:[5,2,1,""],setStatus:[5,2,1,""],updateStatus:[5,2,1,""]},"gssa.session":{GoSmartSimulationServerSession:[5,3,1,""]},"gssa.session.GoSmartSimulationServerSession":{doApi:[5,2,1,""],doCancel:[5,2,1,""],doClean:[5,2,1,""],doCompare:[5,2,1,""],doFinalize:[5,2,1,""],doInit:[5,2,1,""],doProperties:[5,2,1,""],doRequestDiagnostic:[5,2,1,""],doRequestFiles:[5,2,1,""],doRequestResults:[5,2,1,""],doRetrieveStatus:[5,2,1,""],doSearch:[5,2,1,""],doStart:[5,2,1,""],doTmpValidation:[5,2,1,""],doUpdateFiles:[5,2,1,""],doUpdateSettingsXml:[5,2,1,""],onJoin:[5,2,1,""],onRequestAnnounce:[5,2,1,""],onRequestIdentify:[5,2,1,""]},"gssa.sftp_transferrer":{SFTPTransferrer:[5,3,1,""]},"gssa.sftp_transferrer.SFTPTransferrer":{configure_from_xml:[5,2,1,""],connect:[5,2,1,""],disconnect:[5,2,1,""],pull_files:[5,2,1,""],push_files:[5,2,1,""]},"gssa.shadow_watcher":{observe:[5,4,1,""]},"gssa.tmp_transferrer":{TmpTransferrer:[5,3,1,""]},"gssa.tmp_transferrer.TmpTransferrer":{configure_from_xml:[5,2,1,""],connect:[5,2,1,""],disconnect:[5,2,1,""],pull_files:[5,2,1,""],push_files:[5,2,1,""]},"gssa.translator":{GoSmartSimulationTranslator:[5,3,1,""]},"gssa.translator.GoSmartSimulationTranslator":{get_files_required:[5,2,1,""],translate:[5,2,1,""]},"gssa.utils":{get_default_gateway:[5,4,1,""]},gssa:{client:[5,0,0,"-"],comparator:[6,0,0,"-"],config:[5,0,0,"-"],database:[5,0,0,"-"],definition:[5,0,0,"-"],docker:[5,0,0,"-"],error:[5,0,0,"-"],families:[7,0,0,"-"],family:[5,0,0,"-"],http_transferrer:[5,0,0,"-"],parameters:[5,0,0,"-"],server:[5,0,0,"-"],session:[5,0,0,"-"],sftp_transferrer:[5,0,0,"-"],shadow_watcher:[5,0,0,"-"],tmp_transferrer:[5,0,0,"-"],transferrer:[5,0,0,"-"],translator:[5,0,0,"-"],utils:[5,0,0,"-"]}},objnames:{"0":["py","module","Python module"],"1":["py","attribute","Python attribute"],"2":["py","method","Python method"],"3":["py","class","Python class"],"4":["py","function","Python function"],"5":["py","exception","Python exception"]},objtypes:{"0":"py:module","1":"py:attribute","2":"py:method","3":"py:class","4":"py:function","5":"py:exception"},terms:{"_build":17,"abstract":[1,6,12],"boolean":12,"break":5,"case":[6,9,10,12,16,23,24],"catch":24,"class":[5,6,7,18,20,26],"default":[4,5,16,22,24],"enum":[5,12],"final":[5,24],"float":12,"function":6,"import":[5,15,17],"int":5,"long":3,"new":[1,5,14,16,17,24],"null":[12,22],"public":4,"return":[5,6,9,13,16,18,24],"true":[5,7],"while":[0,4,9,12,16,24],abil:5,abl:6,about:[1,9,24],abov:[6,24],absolut:26,access:[3,5,14,15,16,24],accordingli:[18,24],account:13,accur:[9,19],achiev:16,across:18,activ:24,active_count:5,active_simul:5,adapt:3,add:[5,20,23,24],add_algorithm:6,add_input:5,add_paramet:6,addit:[5,24],addition:24,addorupd:5,addpid:7,address:5,adequ:9,administr:[0,9,16],affect:4,affero:4,after:[5,16,23,24],afterward:24,against:[13,16,24],agplv3:4,agreement:0,aioeventhandl:5,akin:9,algorithmdefinit:9,all:[5,12,15,18,23],allow:[0,1,2,4,13,14,16,20,24,25,26],allow_resync:5,almost:5,along:6,alreadi:5,also:[2,3,5,6,19,20,23,24],alter:[0,1],altern:[4,5,26],although:[5,12],alwai:[5,12],ani:[3,4,5,9,12,16,17,18,19,23,24],announc:24,anoth:[3,6,12,13,20],anyth:[5,12,18],apach:0,api:[5,24],apidoc:17,app:18,appear:[5,12],appli:[2,4,12],applic:[5,9,24],applicationsess:5,approach:5,appropri:24,approxim:19,apt:3,arbitrari:[6,18],archiv:[5,26],arg:[5,7],argnam:9,argument:[],arm:4,around:0,arrai:[5,12],assum:[5,26],asynchron:[5,24],asyncio:[5,24],attach:[3,12,24],attack:16,attribut:[],authent:23,author:[0,3,9,24],autobahn:[5,24],autom:15,automat:[16,18],avail:[2,3,4,5,24],awar:24,back:[5,16,18,24,26],backend:[0,1,5],background:[],backward:5,bar:12,base:[0,1,2,3,5,6,7,13],baseeventloop:5,basenam:24,basesess:5,basic:[5,12,18,19,24],basictyp:12,basictype1:12,basictype2:12,baw:7,bear:[5,12],becom:[16,17,26],been:[2,24,25],befor:[5,24,26],begin:24,behav:23,behaviour:[12,24],behind:5,believ:4,beneath:18,better:5,between:[3,6,18,24,25],bit:5,block:5,bodi:[9,20],bool:5,both:[1,3,5,16,20,24],boundari:20,bridg:5,bug:[16,24],build:[],builder:5,built:3,bump:5,bundl:5,calculu:9,call:[5,9,16,24],call_soon_threadsaf:5,callback:5,can:[0,1,5,9,12,18,22],cancel:[1,5,7,18],cancer:[0,1],cannot:18,canon:5,capabl:[13,15,23],care:24,cast:5,categor:5,caught:18,caution:18,cdm:[6,9,12,13],certain:[5,16,24],certainli:5,cgal:[],chanc:5,chang:5,check:[5,16],choic:12,choos:4,chosen_server_nam:2,clarifi:4,clean:[5,7,23,24],client:[],client_directory_prefix:5,clinician:12,clone:[2,3],close:5,clsname:5,cmake:2,cmake_install_prefix:2,code:[0,3,4,5,6,11,18,19,21,22],coexist:12,collabor:0,collect:20,column:[12,22],com:[3,5,24],combin:[9,12,16],command:[2,3,5],commiss:0,common:5,commun:[4,5,19,24],complet:[5,6,18,22,24],compon:[0,6,12,19,24],compos:3,comprehens:3,compris:[2,19,24],comput:0,concept:[3,12],conceptu:[0,13],concern:9,concret:[],concurr:[],condit:9,config_fil:5,configfilenam:7,configur:[],configure_from_xml:5,confirm:5,conjunct:26,connect:[3,5,23,24],consequ:12,conserv:18,consid:[3,4],consist:16,consortium:[3,4],constant:[9,12],constitut:19,consum:5,contact:[3,4,23],container:[3,4,16],content:[],contigu:20,control:[],convent:9,convention:9,convert:15,convert_paramet:5,copi:[4,5],copy_output:5,core:[3,5,15],coro:5,coroutin:24,correl:24,correspond:[0,12,19],could:[5,12],cours:19,cover:4,creat:[5,12,14,16,17,22],create_xml_from_str:5,created_at:22,creep:16,critic:16,crossbar:25,current:[0,2,3,5,16,23,24,26],currentneedlelength:6,daemon:[3,5,16],data:[1,2,9,19],databas:[],date:26,dcmake_install_prefix:2,dct:5,debug:[7,26],def:23,defin:[1,6,9,12,20,24,26],definition_fil:5,delet:[5,22],deliv:23,denial:16,depend:[],deprec:5,deriv:4,describ:[6,11,12,20,23],descript:[],design:[1,2],dest:5,destin:[5,7],destinationstr:5,destinationurl:[5,26],destroi:5,detail:[2,5,13],dev:2,develop:[2,3,14,18,19,23],dfamili:20,dfile:20,diagnost:[1,5],dict:5,dictionari:5,dif:[6,13],diff:[6,13],differ:[5,9,12,13,24],difficulti:2,direct:[15,25],directli:[4,11],directori:[2,5,19,20,22,23,24],disconnect:5,discoveri:24,distinct:20,distinguish:18,dle:[],doapi:5,doc:17,docancel:5,docker:[],dockerfamili:7,dockerfil:2,dockerlaunch:[2,3,5,16],dockerlaunchd:2,doclean:5,docompar:5,docstr:17,doe:[3,4,5,12,24],dofin:5,doinit:5,dolfin:15,don:5,doproperti:5,dorequestdiagnost:5,dorequestfil:5,dorequestresult:5,doretrievestatu:5,dosearch:5,dosimul:5,dostart:5,dot:5,dotmpvalid:5,doupdatefil:5,doupdatesettingsxml:5,down:6,download:5,downloadfil:5,dummi:[5,24],dundalk:0,dynam:[0,1],e_cancel:18,e_client:18,e_model:18,e_serv:18,e_unknown:18,each:[5,12,13,19,20,24,25],earliest:5,eas:4,easi:0,easili:14,effect:22,either:[5,20],element:[5,12,15],elementtre:5,elmer:[0,2,3,7],elmer_binari:7,elmer_libnuma:[],elmer_libnuma_legaci:[],elmerlibnumafamili:7,elmerlibnumalegacyfamili:7,els:5,embed:[13,20],empti:23,enabl:[2,3,4,24],encod:12,end:[2,12,16],endpoint:5,engin:[0,12],enough:6,ensur:[3,5,12,16],entir:[2,16],entiti:12,entri:[5,12,22,24],environ:16,equal:6,equip:[0,1],equival:[6,24],err:18,error:[],error_statu:24,errorexcept:5,errormessag:5,especi:[3,12,24],essenti:[5,12,16],establish:24,estim:5,etc:[5,12,23],etc_loc:5,etre:5,european:0,even:9,event:[5,24],eventcomplet:5,eventfail:5,everyth:5,exact:[12,20],examin:5,exampl:[9,19],except:[4,5,9,18,24],execut:[],exemplar:[4,16],exist:[0,2,3,4,5,23,24],exists_onli:5,exit:[5,22,23],exit_cod:[5,22],expect:[9,23,24],explicitli:4,exposur:16,extend:19,extens:24,extern:[18,19],extract:5,facilit:0,fact:16,fail:[5,24],failur:[5,24],fall:5,fals:[5,7],famili:[],family_nam:[5,7],familytyp:5,fashion:12,fault:5,feedback:18,fenic:[],fenicsfamili:[7,16],fenicsproject:15,few:[],field:[12,20],file1:13,file2:13,file:[4,5,6,13,15,16,17,19,20,23,24,26],filenam:[5,20],files_requir:[5,7],filesystem:5,filesystemeventhandl:5,fill:12,find:[2,5,19,24],finit:15,fire:5,first:[0,5,13,24],fixm:5,flag:22,fledg:19,flexibl:12,folder:5,follow:[3,9,12,22,24,26],form:[5,9,12,20],format:[],former:5,forth:[6,12],forward:[24,26],found:5,framework:[0,1,3,15,19],free:5,friendli:3,from:[1,2,4,5,9,12,14,15,18,19,20,22,24,26],full:[5,23],fulli:[19,24],fullpath:5,fund:0,fundament:6,further:2,futur:18,gatewai:5,gather_diagnost:5,gather_result:5,gener:[2,4,6,15,16,18,20,24],geometr:[1,6],geometri:[6,13],get:[3,5],get_api_vers:5,get_config_fil:5,get_default_gatewai:5,get_dir:5,get_error:5,get_exit_statu:5,get_fil:5,get_files_requir:5,get_guid:5,get_needle_paramet:[5,7],get_paramet:[5,7],get_percentage_socket_loc:7,get_remote_dir:5,getproperti:5,getstatusandvalid:5,getvalid:5,gfoam:7,gfoamfamili:7,ghp:17,git:[2,3,17],github:[2,3,4,17],give:5,given:[4,5,12,13,19,24],global:[5,24],glossia:[],glot:[0,3,5],glue:4,gmsh:2,gnu:4,goosefoot:[3,4],gosmart:[0,1,3,4],gosmartclienterror:18,gosmarterror:[18,24],gosmartmodelerror:18,gosmartservererror:18,gosmartsimul:[5,24],gosmartsimulationclientcompon:5,gosmartsimulationdefinit:5,gosmartsimulationframeworkargu:7,gosmartsimulationservercompon:5,gosmartsimulationserversess:5,gosmartsimulationtransl:5,got:5,gplv2:4,grab:5,grant:0,group:[6,12,16,19,20],gssa:[],gssa_fil:[5,23],gssa_xml_to_definit:6,gssf:[6,9,16,18,19,20,23,24],gssf_argument:[],guarante:24,guid:[3,5,16,22,24],guid_start:5,hachiko:5,handi:5,handl:[5,20,24,26],have:[2,4,5,9,12,20,23,24,25],heavi:5,held:24,help:[18,23],helper:6,here:[5,11,20,24],hierarch:[5,12],higher:[5,19],highli:19,highlight:5,hoc:5,hold:12,home:0,host:[2,3,16,23],how:[5,6,20],howev:[2,4,6,18,20,24],html:17,http:[],httptransferr:[5,26],human:[6,13,20],hybrid:16,hypermodel:0,hypomodel:0,ideal:6,idempot:5,ident:12,identifi:[2,20,24],ignor:23,ignore_develop:5,illog:18,imag:[0,3,4,5,15,16,19],implement:[6,24],improv:[4,26],in_progress:[5,18],inc:6,includ:[0,4,9,15,16,19,23,24],inclus:4,incompat:[4,5],inconsist:5,incorpor:[4,6,12,15,20,24],index:[0,5,6,17,20],indic:[],individu:4,infer:4,inform:[0,1,5,6,14,22,24],ing:13,init:[5,24],init_config:5,init_logg:5,init_mesh:7,init_percentage_socket_serv:5,input:[1,5,6,16,18,20,23,24,26],input_fil:5,inputfilenam:20,insert:24,insid:[5,16],instal:[],installation_target:2,instanc:[3,5,9,12,16,20],instead:12,instruct:[2,5,19],integ:[5,12,20,22],integr:24,intend:[3,5,19],intent:19,intepret:18,interact:25,interchang:[0,1],interest:3,interfac:[0,1,3,5,12],intern:16,interpret:[5,12,19],intervent:16,introduct:[],invalid:12,invas:[0,1],ireland:0,issu:[2,4,18],itself:[6,13,16,20,23],join:[5,20],json:[5,12],just:5,kei:[5,6,7,23],key_fil:23,keyword:[],kill:16,know:9,known:[5,16,22,24],kwarg:[5,7],label:[4,6],lambda:[6,9],languag:[9,25],last:[22,24],last_status_timestamp:24,later:5,latest:5,launch:[2,3,5,16,24],launcher:[],leakag:9,least:[12,19],leavetre:7,left:13,left_text:6,legaci:7,length:4,less:[9,18],level:[0,16,19,26],libjsoncpp:2,libnuma:7,librari:[3,15,20,24],librarytyp:20,licenc:4,lie:5,lieu:16,lift:5,like:[5,6],limit:[5,12],line:[],link:12,list:[2,5,20,24],listen:24,load:[5,13,24],load_core_definit:5,load_definit:7,local:[2,3,5,23,26],locat:[5,6,16,19,22,24,26],lock:5,log:5,longer:19,look:5,loop:5,lowercas:12,ltd:0,lxml:5,machin:[3,5,24,26],made:[4,5],magic_script:5,mai:[2,3,4,5,9,12,18,19,20,24],main:[5,24],mainli:5,maintain:24,make:[2,4,5,17],make_cal:5,makeerror:5,manag:[3,5],mani:[5,12,15,16,18],manipul:24,manual:16,map:24,mark:5,markallold:5,markdown:17,matc:[4,6,9],match:[5,12,18],mathemat:18,mean:[16,19,26],media:10,mediat:24,medic:12,medium:26,member:[9,20],mesh:[4,7,15,16,19,24],mesher:[15,16,19],mesher_gssf:[],meshergssfmixin:[7,16],messag:[5,6,23],metaclass:5,method:[5,24,26],methodolog:[],mict:[0,1],might:[5,24],migrat:19,mind:[2,5,12],minim:[0,1,16],mix:16,mixin:16,mkdir:2,model:[],modif:[0,2,4],modul:[],moment:5,monitor:1,more:[0,1,4,6,9,12,14,16,19,24],moreov:[3,13,16],most:[5,24],mount:16,move:26,msh:[15,16],much:24,multipl:12,munkr:2,must:[5,9,12,16],name:[5,6,9,12,13,20,23],namespac:[5,16],nativ:[],ncl:20,neatli:5,necessari:[16,19],necessarili:24,nee:[],need:[3,5,6,10,24,26],needl:[5,6,12,20],needle_index:[5,7],network:[4,24,26],nfile:20,nicer:6,nix:20,node:[5,9,20,23,26],non:[6,12,13],none:[5,6,7],normal:[3,4,5,10,26],notabl:4,note:[3,4,5,9,13,19,20,24],notif:24,notifi:24,notify_output:5,nproc:7,nth:5,numa:[0,2],number:[0,16,24],nume:[],numer:[0,1,4,5,6,9,12,13,18],numerical_model:6,numericalmodel:[6,20],numpi:0,object:[5,6,7,12,13],observ:5,observablemixin:5,occur:[5,16],off:5,often:10,omit:2,on_mov:5,onc:[5,16],oncomplet:5,onfail:5,onjoin:5,onleav:5,onli:[],onrequestannounc:5,onrequestidentifi:5,onstatu:5,onto:2,open:3,oper:4,orchestr:[0,1,16],order:[5,20],ordin:[5,20],org:22,organ:[10,20],origin:[17,18],orphan:16,other:[4,6,13,19,25,26],otherwis:[5,12,20],our:[0,4,24],out:[2,5,23,26],outfilenam:7,output:[5,13,23,24,26],output_fil:5,outputhandl:5,over:[4,12,24],overview:0,own:[3,4],page:[0,17],pair:[12,19],paramattrtyp:12,paramattrvalu:12,paramet:[],parameterid:12,paramnam:12,parramattrvalu:12,pars:[],part:[6,11,16,19,24],parti:[4,5,9],partial:26,particular:24,particularli:[12,26],pass:[4,5,12,13,18,22,24],past:22,path:26,pattern:[5,24],pde:15,per:[2,16],percentag:[5,22,24],percutan:6,perhap:5,permit:[5,24],persist:[2,24],perspect:9,phantom:10,physic:[0,1,10,12,18],pick:12,piec:[5,14],pip:3,place:[5,9,10,16],placehold:[],platform:[0,1],pleas:[3,4],plug:19,point:[2,24],polici:4,port:[2,3,5,23],possibl:[5,6,12,24],post:5,potenti:12,ppa:15,pre:[4,19,24],precaut:9,prematur:5,prepar:[4,5,12,24],prepare_simul:7,present:[0,5,16,22,24,26],prevent:12,primari:0,primarili:[5,17,23,26],print:5,prior:16,privileg:19,problem:18,procedur:[6,9,10,12,24],process:[3,6,23,24],processor:24,produc:[5,6],programm:18,progress:[1,5],progress_statu:24,project:[0,1,3,4],prompt:12,proof:3,proper:19,properti:[5,24],proprietari:4,protect:[16,24],protocol:[5,12,24],prove:24,proven:9,provid:[0,1,4,5,6,9,12,15,16,18,20,24,25],pub:24,publicli:[],publish:[0,5,24],publish_cb:5,pull:[3,5],pull_fil:5,purpos:[12,15,25,26],push:[5,17],push_fil:5,put:24,python:[],pythonocc:2,pyyaml:2,quickstart:[],radiolog:3,rate:5,reach:24,read_paramet:5,readabl:[6,13,20,24],reader:5,readi:[3,24],real:22,reason:[5,18],receiv:6,receive_respons:5,recognis:24,recommend:[2,25],record:[2,5,12,22],reduc:16,redund:16,ref:5,refer:[],referenc:[12,23],refus:[5,16],regener:17,region:[6,20],regist:[2,5,23,24],reinstat:26,rel:24,relat:[24,25],relax:4,releas:[4,5],relev:[3,4,11,16,26],reliabl:24,remain:[4,5,24],remot:[0,5,24],remote_dir:5,remote_root:[5,26],remov:[5,16,24],render:12,repetit:6,repli:[5,24],report:[5,24],repositori:4,repres:[6,12,19],represent:[5,12],request:[5,9,23,24],request_announc:[5,24],request_diagnost:5,request_fil:[5,24],request_identifi:[5,24],request_result:5,requir:[4,5,12,16,19,24],research:[0,1],resourc:20,respect:[4,5],respond:24,respons:[3,5,12,18,24],restart:[2,3,16,24],restructuredtext:17,result:[5,6,9],resum:22,retriev:[1,5],retrieve_fil:7,retrieve_statu:[5,24],reusabl:4,rformat:20,rgroup:20,ricalmodel:[],rid:20,right:13,right_text:6,rinput:20,risk:16,rname:20,root:[5,6],router:[],routin:[5,18,24],row:[5,22],rpc:[5,24],rst:[],run:[3,5,6,9,12,16,19,23,24],run_script:5,runtimeerror:5,sai:[6,12],same:[3,13,16,19,22,24],sampl:[10,25],sandbox:19,scan:[7,19],schedul:5,schema:20,scheme:16,scientif:15,score:[5,24],script:[5,13,15,23],search:[0,5],second:[13,26],section:[12,26],secur:[3,9,26],see:[1,2,4,6,14,16,20],seen:12,select:[12,20],send:[1,5,6,24],send_command:5,sent:5,separ:[2,5,6,13,19,24],seri:[6,15,24],server:[],server_hostnam:24,server_id:[5,24],servic:[0,4,16],session:[],set:[0,4,5,6,12,16,24,26],set_exit_statu:5,set_numerical_model:6,set_remote_dir:5,set_transferr:6,set_update_socket:5,setdatabas:5,setstatu:5,setting_final_timestep:12,setup:[3,16],sftp:[],sftp_host:23,sftp_port:23,sftptransferr:[5,26],should:[3,4,5,6,9,12,15,16,17,19,20,23,24,26],show:23,shutdown:5,sid:23,side:[3,5,12,18,24],sif:4,silent:7,simdata_path:5,similar:12,similarli:4,simpl:[1,13,20],simplic:17,simulation_definit:[],simulation_id:24,simulationdefinit:[6,13,20],simultan:16,singl:[5,19],situat:16,skip:[5,23],skip_clean:5,slightli:[12,19],slow:5,slug:9,small:0,sock:7,socket:[5,16,24],socket_loc:5,soft:[5,22],softwar:[0,14],sole:9,solid:20,solut:15,solver:[3,12,13,16],some:[4,5],someth:9,sort:5,sourc:[2,3,4,5,6,7,19,20,25],sourcepath:5,sourceurl:26,sourceurlstr:5,space:9,special:24,specif:[2,4,5,12,19,20,22,23],specifi:[9,12,20,26],sphinx:17,sponsor:3,sqlite:22,sqlitesimulationdatabas:5,stabl:[0,3,15,16],standalon:0,standard:[5,16],start:[2,3,5,15,16,24],statu:[5,22,24],status:22,status_socket:7,step:[5,16],still:[2,5,19],stl:20,stop:[5,16],str:5,straightforward:3,strategi:[0,1],stricter:4,strictli:[6,10,16],string:[5,12,24],sub:24,subclass:[5,19],subdir:23,subdirectori:[5,23,25],subdomain:[6,20],subject:4,submiss:4,submit:5,submitt:5,subscrib:[5,24],subsequ:3,success:[5,18],success_statu:24,sudo:[3,16],suffix:5,suit:3,summari:5,supplement:5,suppli:[2,9,12,19,20],support:[0,3,24],sure:2,surfac:[20,23],synopsi:5,syntact:18,system:[2,3,5,19,26],tag:20,take:[6,9,10,12,13,16,23],tar:[20,23,26],target:[5,24],task:18,taverna:0,technic:12,technician:[0,1],technolog:[0,1,3],tell:5,templat:[4,6],temporari:5,term:[4,19],test:[0,2,3,23,24],text:[22,23],textual:[6,9],than:[9,19,24,26],that_xml:5,thei:[5,9,10,19,20,24],them:[16,20,23],themselv:19,theoret:11,theori:18,therebi:12,thi:[0,1,2,3,4,5,6,9,10,12,13,15,16,17,18,19,20,23,24,25,26],third:[4,5,9],this_xml:5,those:[5,12],thread:24,through:[0,1,4,5,24,25,26],thrown:18,tidi:16,tie:6,time:[5,6,9,12,22,24],timeout:24,timestamp:[5,22,24],tinyint:22,tmp:[],tmpdir:5,tmptransferr:[5,26],to_list:7,to_mesh_xml:7,to_xml:7,toc:[],todo:[5,6,19,26],told:5,too:16,tool:[0,3,4,5,9,12,13,18,19],traffic:3,transfer:[5,24,26],transferr:[],translat:[],transmiss:24,trasferr:26,treat:20,treatment:[0,1],tree:[20,25],trigger:[5,18,24],tripl:12,trivial:5,trust:19,truthi:23,try_json:[5,7],tumour:20,tupl:[5,12],turn:5,two:[5,13,16,19,24],txaio:5,typ:[5,6],type:[],typic:5,ubuntu:[2,3],ultim:9,unabl:13,uncertain:18,under:[0,4,26],underscor:9,understand:[6,9,13],unfinish:5,unhandl:24,unifi:18,uniqu:[12,20,24],univers:12,unknown:18,unless:[5,12],unnecessari:16,unprivileg:19,unspecifi:9,unsupport:14,until:24,unusu:0,unwieldi:5,unzip:26,updat:[5,7,16,22,26],update_callback:5,update_fil:[5,24],update_settings_xml:[5,24],update_statu:24,update_status_callback:5,updatestatu:5,updatevalid:5,upload:[5,17],uploadfil:5,upper:9,upstream:[4,15],url:[5,6,26],urllib:5,usabl:26,usag:[],use_observ:5,user:[2,12,16,18,19,24],usr:5,usual:[5,6],uuid:[23,24],valid:[5,7,9,10,12,22],validation_xml:[5,24],valu:[5,6,12],variat:12,variou:25,veri:[3,18],verifi:2,version:[5,13,17],via:[0,2,3,4,5,23,24],vigil:24,visibl:17,vivo:10,volum:5,volumetr:[15,16,20],vtk:2,vtp:20,wai:[6,19,20],wait:5,wait_for_respons:5,wamp:[],wamp_rout:2,want:2,watchdog:5,web:[0,1,3,25],websit:0,websocket:[2,23],websocket_port:23,webus:[],well:[3,9],what:5,when:[5,12,24],where:[4,5,12,18,19],wherev:5,whether:5,which:[4,5,10,13,18,19,20,23,24],whichev:5,whitelist:3,whole:12,why:18,wide:[2,5],wider:0,widget:12,win:12,wish:[18,23],within:[0,2,4,9,12,15,20,25],without:[16,24],work:[0,4,5,18,22,23,24],workflow:[],working_directori:[5,7,24],would:[3,6,16,19,24],wrap:[3,5,14,16,18,23],wrapped_coroutin:5,wrapper:13,write:[19,26],writer:5,written:12,www:[0,1,19,22],xml1:24,xml2:24,xml:[],xml_string:5,yaml:5,yet:18,yml:5,you:[2,3,4,22,23],your:[3,4,24],zone:20},titles:["Glossia","Introduction","Native Installation","Quickstart","License","gssa package","gssa.comparator package","gssa.families package","src","Go-Smart Simulation Algorithms","Clinical Domain Model - Contexts","Go-Smart Clinical Domain Model","Go-Smart Simulation Parameters","Comparison of GSSA-XML documents","Go-Smart Simulation Architecture - Python Docker Container Module","Go-Smart Simulation Architecture - FEniCS Family","Go-Smart Simulation Architecture - Docker Workflows","Documentation workflow","Error types","Go-Smart Simulation Model Families","Go-Smart Simulation Architecture XML Format (GSSA-XML)","Reference","Go-Smart Simulation Server Database","Executables","Go-Smart Simulation Architecture - Simulation Server","Go-Smart Simulation Architecture - WAMP Router","Transferrers"],titleterms:{aka:0,algorithm:9,architectur:[0,14,15,16,20,24,25],argument:23,attribut:12,background:[],build:2,caveat:16,cgal:16,client:[5,23],clinic:[10,11],compar:[6,13],comparison:13,concret:12,concurr:24,config:5,configur:26,contain:[3,14,16],content:[0,5,6,7],context:10,control:24,databas:[5,22],definit:[5,9,15,16],depend:[2,3],descript:23,docker:[5,7,14,16],document:[13,17],domain:[10,11],elmer_libnuma:7,elmer_libnuma_legaci:7,error:[5,18],execut:[3,23],famili:[5,7,15,19],fenic:[7,15],format:20,glossia:0,gssa:[0,5,6,7,13,20],gssf_argument:7,http:26,http_transferr:5,indic:0,instal:2,interact:3,introduct:1,licens:4,mesher_gssf:7,methodolog:13,model:[10,11,19],modul:[5,6,7,14],nativ:2,onli:16,option:23,packag:[5,6,7],paramet:[5,12],pars:6,placehold:12,posit:23,prune:16,python:14,quickstart:3,refer:21,router:25,server:[5,22,23,24],session:5,sftp:26,sftp_transferr:5,shadow_watch:5,simul:[0,3,9,12,14,15,16,19,20,22,23,24,25],simulation_definit:6,smart:[0,9,11,12,13,14,15,16,19,20,22,23,24,25],src:8,submodul:[5,6,7],subpackag:5,tabl:0,tmp:26,tmp_transferr:5,transferr:[5,26],translat:5,type:[12,18],usag:[2,13],util:5,variant:16,wamp:25,workflow:[16,17],xml:[13,20]}})