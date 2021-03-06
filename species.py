base_url = 'ftp://ftp.ensembl.org/pub/release-80/fasta/'

species_dict = {
    "ailuropoda_melanoleuca": base_url + "ailuropoda_melanoleuca/cdna/Ailuropoda_melanoleuca.ailMel1.cdna.all.fa.gz",
    "anas_platyrhynchos": base_url + "anas_platyrhynchos/cdna/Anas_platyrhynchos.BGI_duck_1.0.cdna.all.fa.gz",
    "anolis_carolinensis": base_url + "anolis_carolinensis/cdna/Anolis_carolinensis.AnoCar2.0.cdna.all.fa.gz",
    "arabidopsis_thaliana": "http://bio.math.berkeley.edu/kallisto/transcriptomes/Arabidopsis_thaliana.TAIR10.28.cdna.all.fa.gz",
    "astyanax_mexicanus": base_url + "astyanax_mexicanus/cdna/Astyanax_mexicanus.AstMex102.cdna.all.fa.gz",
    "bos_taurus": base_url + "bos_taurus/cdna/Bos_taurus.UMD3.1.cdna.all.fa.gz",
    "caenorhabditis_elegans": base_url + "caenorhabditis_elegans/cdna/Caenorhabditis_elegans.WBcel235.cdna.all.fa.gz",
    "callithrix_jacchus": base_url + "callithrix_jacchus/cdna/Callithrix_jacchus.C_jacchus3.2.1.cdna.all.fa.gz",
    "canis_familiaris": base_url + "canis_familiaris/cdna/Canis_familiaris.CanFam3.1.cdna.all.fa.gz",
    "cavia_porcellus": base_url + "cavia_porcellus/cdna/Cavia_porcellus.cavPor3.cdna.all.fa.gz",
    "chlorocebus_sabaeus": base_url + "chlorocebus_sabaeus/cdna/Chlorocebus_sabaeus.ChlSab1.1.cdna.all.fa.gz",
    "choloepus_hoffmanni": base_url + "choloepus_hoffmanni/cdna/Choloepus_hoffmanni.choHof1.cdna.all.fa.gz",
    "ciona_intestinalis": base_url + "ciona_intestinalis/cdna/Ciona_intestinalis.KH.cdna.all.fa.gz",
    "ciona_savignyi": base_url + "ciona_savignyi/cdna/Ciona_savignyi.CSAV2.0.cdna.all.fa.gz",
    "danio_rerio": base_url + "danio_rerio/cdna/Danio_rerio.GRCz10.cdna.all.fa.gz",
    "dasypus_novemcinctus": base_url + "dasypus_novemcinctus/cdna/Dasypus_novemcinctus.Dasnov3.0.cdna.all.fa.gz",
    "dipodomys_ordii": base_url + "dipodomys_ordii/cdna/Dipodomys_ordii.dipOrd1.cdna.all.fa.gz",
    "drosophila_melanogaster": base_url + "drosophila_melanogaster/cdna/Drosophila_melanogaster.BDGP6.cdna.all.fa.gz",
    "echinops_telfairi": base_url + "echinops_telfairi/cdna/Echinops_telfairi.TENREC.cdna.all.fa.gz",
    "equus_caballus": base_url + "equus_caballus/cdna/Equus_caballus.EquCab2.cdna.all.fa.gz",
    "erinaceus_europaeus": base_url + "erinaceus_europaeus/cdna/Erinaceus_europaeus.HEDGEHOG.cdna.all.fa.gz",
    "felis_catus": base_url + "felis_catus/cdna/Felis_catus.Felis_catus_6.2.cdna.all.fa.gz",
    "ficedula_albicollis": base_url + "ficedula_albicollis/cdna/Ficedula_albicollis.FicAlb_1.4.cdna.all.fa.gz",
    "gadus_morhua": base_url + "gadus_morhua/cdna/Gadus_morhua.gadMor1.cdna.all.fa.gz",
    "gallus_gallus": base_url + "gallus_gallus/cdna/Gallus_gallus.Galgal4.cdna.all.fa.gz",
    "gasterosteus_aculeatus": base_url + "gasterosteus_aculeatus/cdna/Gasterosteus_aculeatus.BROADS1.cdna.all.fa.gz",
    "gorilla_gorilla": base_url + "gorilla_gorilla/cdna/Gorilla_gorilla.gorGor3.1.cdna.all.fa.gz",
    "homo_sapiens": base_url + "homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz",
    "ictidomys_tridecemlineatus": base_url + "ictidomys_tridecemlineatus/cdna/Ictidomys_tridecemlineatus.spetri2.cdna.all.fa.gz",
    "latimeria_chalumnae": base_url + "latimeria_chalumnae/cdna/Latimeria_chalumnae.LatCha1.cdna.all.fa.gz",
    "lepisosteus_oculatus": base_url + "lepisosteus_oculatus/cdna/Lepisosteus_oculatus.LepOcu1.cdna.all.fa.gz",
    "loxodonta_africana": base_url + "loxodonta_africana/cdna/Loxodonta_africana.loxAfr3.cdna.all.fa.gz",
    "macaca_mulatta": base_url + "macaca_mulatta/cdna/Macaca_mulatta.MMUL_1.cdna.all.fa.gz",
    "macropus_eugenii": base_url + "macropus_eugenii/cdna/Macropus_eugenii.Meug_1.0.cdna.all.fa.gz",
    "meleagris_gallopavo": base_url + "meleagris_gallopavo/cdna/Meleagris_gallopavo.UMD2.cdna.all.fa.gz",
    "microcebus_murinus": base_url + "microcebus_murinus/cdna/Microcebus_murinus.micMur1.cdna.all.fa.gz",
    "monodelphis_domestica": base_url + "monodelphis_domestica/cdna/Monodelphis_domestica.BROADO5.cdna.all.fa.gz",
    "mus_musculus": base_url + "mus_musculus/cdna/Mus_musculus.GRCm38.cdna.all.fa.gz",
    "mustela_putorius_furo": base_url + "mustela_putorius_furo/cdna/Mustela_putorius_furo.MusPutFur1.0.cdna.all.fa.gz",
    "myotis_lucifugus": base_url + "myotis_lucifugus/cdna/Myotis_lucifugus.Myoluc2.0.cdna.all.fa.gz",
    "nomascus_leucogenys": base_url + "nomascus_leucogenys/cdna/Nomascus_leucogenys.Nleu1.0.cdna.all.fa.gz",
    "ochotona_princeps": base_url + "ochotona_princeps/cdna/Ochotona_princeps.pika.cdna.all.fa.gz",
    "oreochromis_niloticus": base_url + "oreochromis_niloticus/cdna/Oreochromis_niloticus.Orenil1.0.cdna.all.fa.gz",
    "ornithorhynchus_anatinus": base_url + "ornithorhynchus_anatinus/cdna/Ornithorhynchus_anatinus.OANA5.cdna.all.fa.gz",
    "oryctolagus_cuniculus": base_url + "oryctolagus_cuniculus/cdna/Oryctolagus_cuniculus.OryCun2.0.cdna.all.fa.gz",
    "oryzias_latipes": base_url + "oryzias_latipes/cdna/Oryzias_latipes.MEDAKA1.cdna.all.fa.gz",
    "otolemur_garnettii": base_url + "otolemur_garnettii/cdna/Otolemur_garnettii.OtoGar3.cdna.all.fa.gz",
    "ovis_aries": base_url + "ovis_aries/cdna/Ovis_aries.Oar_v3.1.cdna.all.fa.gz",
    "pan_troglodytes": base_url + "pan_troglodytes/cdna/Pan_troglodytes.CHIMP2.1.4.cdna.all.fa.gz",
    "papio_anubis": base_url + "papio_anubis/cdna/Papio_anubis.PapAnu2.0.cdna.all.fa.gz",
    "pelodiscus_sinensis": base_url + "pelodiscus_sinensis/cdna/Pelodiscus_sinensis.PelSin_1.0.cdna.all.fa.gz",
    "petromyzon_marinus": base_url + "petromyzon_marinus/cdna/Petromyzon_marinus.Pmarinus_7.0.cdna.all.fa.gz",
    "poecilia_formosa": base_url + "poecilia_formosa/cdna/Poecilia_formosa.PoeFor_5.1.2.cdna.all.fa.gz",
    "pongo_abelii": base_url + "pongo_abelii/cdna/Pongo_abelii.PPYG2.cdna.all.fa.gz",
    "procavia_capensis": base_url + "procavia_capensis/cdna/Procavia_capensis.proCap1.cdna.all.fa.gz",
    "pteropus_vampyrus": base_url + "pteropus_vampyrus/cdna/Pteropus_vampyrus.pteVam1.cdna.all.fa.gz",
    "rattus_norvegicus": base_url + "rattus_norvegicus/cdna/Rattus_norvegicus.Rnor_6.0.cdna.all.fa.gz",
    "saccharomyces_cerevisiae": base_url + "saccharomyces_cerevisiae/cdna/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.gz",
    "sarcophilus_harrisii": base_url + "sarcophilus_harrisii/cdna/Sarcophilus_harrisii.DEVIL7.0.cdna.all.fa.gz",
    "sorex_araneus": base_url + "sorex_araneus/cdna/Sorex_araneus.COMMON_SHREW1.cdna.all.fa.gz",
    "sus_scrofa": base_url + "sus_scrofa/cdna/Sus_scrofa.Sscrofa10.2.cdna.all.fa.gz",
    "taeniopygia_guttata": base_url + "taeniopygia_guttata/cdna/Taeniopygia_guttata.taeGut3.2.4.cdna.all.fa.gz",
    "takifugu_rubripes": base_url + "takifugu_rubripes/cdna/Takifugu_rubripes.FUGU4.cdna.all.fa.gz",
    "tarsius_syrichta": base_url + "tarsius_syrichta/cdna/Tarsius_syrichta.tarSyr1.cdna.all.fa.gz",
    "tetraodon_nigroviridis": base_url + "tetraodon_nigroviridis/cdna/Tetraodon_nigroviridis.TETRAODON8.cdna.all.fa.gz",
    "tupaia_belangeri": base_url + "tupaia_belangeri/cdna/Tupaia_belangeri.TREESHREW.cdna.all.fa.gz",
    "tursiops_truncatus": base_url + "tursiops_truncatus/cdna/Tursiops_truncatus.turTru1.cdna.all.fa.gz",
    "vicugna_pacos": base_url + "vicugna_pacos/cdna/Vicugna_pacos.vicPac1.cdna.all.fa.gz",
    "xenopus_tropicalis": base_url + "xenopus_tropicalis/cdna/Xenopus_tropicalis.JGI_4.2.cdna.all.fa.gz",
    "xiphophorus_maculatus": base_url + "xiphophorus_maculatus/cdna/Xiphophorus_maculatus.Xipmac4.4.2.cdna.all.fa.gz"
}

gene_anno_dict = {
    "ornithorhynchus_anatinus" : "anatinus_gene_ensembl",
    "cavia_porcellus": "cporcellus_gene_ensembl",
    "aculeatus_genes": "gaculeatus_gene_ensembl",   
    "ictidomys_tridecemlineatus": "itridecemlineatus_gene_ensembl", 
    "loxodonta_africana": "lafricana_gene_ensembl",
    "choloepus_hoffmanni": "choffmanni_gene_ensembl",    
    "ciona_savignyi": "csavignyi_gene_ensembl",  
    "felis_catus": "fcatus_gene_ensembl",    
    "rattus_norvegicus": "rnorvegicus_gene_ensembl",     
    "pelodiscus_sinensis": "psinensis_gene_ensembl",     
    "callithrix_jacchus": "cjacchus_gene_ensembl",   
    "tursiops_truncatus": "ttruncatus_gene_ensembl",     
    "saccharomyces_cerevisiae": "scerevisiae_gene_ensembl",  
    "caenorhabditis_elegans": "celegans_gene_ensembl",   
    "chlorocebus_sabaeus": "csabaeus_gene_ensembl",  
    "oreochromis_niloticus": "oniloticus_gene_ensembl",  
    "astyanax_mexicanus": "amexicanus_gene_ensembl",     
    "takifugu_rubripes": "trubripes_gene_ensembl",   
    "petromyzon_marinus": "pmarinus_gene_ensembl",   
    "erinaceus_europaeus": "eeuropaeus_gene_ensembl",    
    "ficedula_albicollis": "falbicollis_gene_ensembl",   
    "echinops_telfairi": "etelfairi_gene_ensembl",   
    "ciona_intestinalis": "cintestinalis_gene_ensembl",  
    "pan_troglodytes": "ptroglodytes_gene_ensembl",  
    "nomascus_leucogenys": "nleucogenys_gene_ensembl",   
    "sus_scrofa": "sscrofa_gene_ensembl",    
    "oryctolagus_cuniculus": "ocuniculus_gene_ensembl",  
    "dasypus_novemcinctus": "dnovemcinctus_gene_ensembl",    
    "procavia_capensis": "pcapensis_gene_ensembl",   
    "taeniopygia_guttata": "tguttata_gene_ensembl",  
    "myotis_lucifugus": "mlucifugus_gene_ensembl",   
    "homo_sapiens": "hsapiens_gene_ensembl",     
    "poecilia_formosa": "pformosa_gene_ensembl",     
    "tupaia_belangeri": "tbelangeri_gene_ensembl",   
    "mustela_putorius": "mfuro_gene_ensembl",    
    "gallus_gallus": "ggallus_gene_ensembl",     
    "xenopus_tropicalis": "xtropicalis_gene_ensembl",    
    "equus_caballus": "ecaballus_gene_ensembl",  
    "pongo_abelii": "pabelii_gene_ensembl",  
    "danio_rerio": "drerio_gene_ensembl",    
    "xiphophorus_maculatus": "xmaculatus_gene_ensembl",  
    "tetraodon_nigroviridis": "tnigroviridis_gene_ensembl",  
    "latimeria_chalumnae": "lchalumnae_gene_ensembl",    
    "ailuropoda_melanoleuca": "amelanoleuca_gene_ensembl",   
    "macaca_mulatta": "mmulatta_gene_ensembl",   
    "pteropus_vampyrus": "pvampyrus_gene_ensembl",   
    "papio_anubis": "panubis_gene_ensembl",  
    "monodelphis_domestica": "mdomestica_gene_ensembl",  
    "anolis_carolinensis": "acarolinensis_gene_ensembl",     
    "vicugna_pacos": "vpacos_gene_ensembl",  
    "tarsius_syrichta": "tsyrichta_gene_ensembl",    
    "otolemur_garnettii": "ogarnettii_gene_ensembl",     
    "drosophila_melanogaster": "dmelanogaster_gene_ensembl",     
    "microcebus_murinus": "mmurinus_gene_ensembl",   
    "lepisosteus_oculatus": "loculatus_gene_ensembl",    
    "oryzias_latipes": "olatipes_gene_ensembl",  
    "ochotona_princeps": "oprinceps_gene_ensembl",   
    "gorilla_gorilla": "ggorilla_gene_ensembl",  
    "dipodomys_ordii": "dordii_gene_ensembl",    
    "ovis_aries": "oaries_gene_ensembl",     
    "mus_musculus": "mmusculus_gene_ensembl",    
    "meleagris_gallopavo": "mgallopavo_gene_ensembl",    
    "gadus_morhua": "gmorhua_gene_ensembl",  
    "sorex_araneus": "saraneus_gene_ensembl",    
    "anas_platyrhynchos": "aplatyrhynchos_gene_ensembl",     
    "sarcophilus_harrisii": "sharrisii_gene_ensembl",    
    "macropus_eugenii": "meugenii_gene_ensembl",     
    "bos_taurus": "btaurus_gene_ensembl",    
    "canis_familiaris": "cfamiliaris_gene_ensembl"
} 

