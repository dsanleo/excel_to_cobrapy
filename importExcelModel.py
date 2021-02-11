import pandas as pd
from cobra import Model, Reaction, Metabolite
from cobra.io import write_sbml_model

MET_SHEET_ID='Metabolite List'
MET_ID_IDX='Abbreviation'
MET_FORMULA_IDX='Charged formula'
MET_NAME_IDX='Description'
MET_COMPARTMENT_IDX='Compartment'
MET_CHARGE_IDX='Charge'
DEFAULT_COMPARTMENT='c'
RXN_SHEET_ID='Reaction List'
RXN_ID_IDX='Abbreviation'
RXN_REACTION_IDX='Reaction'
RXN_NAME_IDX='Description'
RXN_GPR_IDX='GPR'
RXN_SUBSYSTEM_IDX='Subsystem'
RXN_LOWER_BOUND_IDX='Lower bound'
RXN_UPPER_BOUND_IDX='Upper bound'
RXN_OBJECTIVE_IDX='Objective'
DEFAULT_LOWER_BOUND=-1000
DEFAULT_UPPER_BOUND=1000
DEFAULT_OBJECTIVE_COEFF=0

def import_excel_model(file_excel_path, model_id="default_model"):
    # Create a new cobra model
    model = Model(model_id)
    
    #Import metabolites
    model_excel_metabolites=pd.read_excel(file_excel_path,sheet_name=MET_SHEET_ID)
    metabolites_list=list()
    for index,row in model_excel_metabolites.iterrows():
        compartment=row[MET_COMPARTMENT_IDX] if not pd.isna(row[MET_COMPARTMENT_IDX]) else DEFAULT_COMPARTMENT
        metabolite=Metabolite(id=row[MET_ID_IDX],
                  formula=row[MET_FORMULA_IDX],
                  name=row[MET_NAME_IDX],
                  compartment=compartment,
                  charge=row[MET_CHARGE_IDX])
        metabolites_list.append(metabolite)
    # Add metabolites to the model
    model.add_metabolites(metabolites_list)
    
    #Import reactions
    model_excel_reactions=pd.read_excel(file_excel_path,sheet_name=RXN_SHEET_ID)

    for index,row in model_excel_reactions.iterrows():
        if not pd.isna(row[RXN_ID_IDX]):
            lb=row[RXN_LOWER_BOUND_IDX] if not pd.isna(row[RXN_LOWER_BOUND_IDX]) else DEFAULT_LOWER_BOUND
            ub=row[RXN_UPPER_BOUND_IDX] if not pd.isna(row[RXN_UPPER_BOUND_IDX]) else DEFAULT_UPPER_BOUND
            objective_coeff=row[RXN_OBJECTIVE_IDX] if not pd.isna(row[RXN_OBJECTIVE_IDX]) else DEFAULT_OBJECTIVE_COEFF
            reaction=Reaction(id=row[RXN_ID_IDX],
                                 name=row[RXN_NAME_IDX],
                                 subsystem=row[RXN_SUBSYSTEM_IDX],
                                 lower_bound=lb,
                                 upper_bound=ub)

            # Add Genes
            if not pd.isna(row[RXN_GPR_IDX]):
                reaction.gene_reaction_rule=row[RXN_GPR_IDX]

            # Add the reaction to the model
            model.add_reaction(reaction)

            # Include the reaction              
            try:
                model.reactions.get_by_id(row[RXN_ID_IDX]).build_reaction_from_string(row[RXN_REACTION_IDX])
            except Exception as e:
                print("Error parsing %s string '%s'" % (repr(rxn), rxn_str))
                raise e 

            # Include the objective coefficient
            model.reactions.get_by_id(row[RXN_ID_IDX]).objective_coefficient=objective_coeff
        else:
            print("The row: "+index+" is empty or doesn't have id.")
        
    return(model)

def excel_to_sbml(file_excel_path, file_sbml_path,model_id="default_model",**kwargs):
    write_sbml_model(import_excel_model(file_excel_path,model_id),file_sbml_path,**kwargs)


