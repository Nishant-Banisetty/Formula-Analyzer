from openpyxl.formula import Tokenizer

function_with_criteria = {
    "IF(": 1,
}


class FormulaTokens:
    def __init__(self, tid, tvalue, ttype, tsubtype, tlevel, tcriteria):
        self.tvalue = tvalue
        self.ttype = ttype
        self.tsubtype = tsubtype
        self.tlevel = tlevel
        self.tcriteria = tcriteria
        self.tid = tid


def token_list_update(token_list):
    list_obj = []
    criteria_flg = False
    current_criteria_pos = []

    if token_list:
        for t in token_list:

            if t.ttype == "OPERATOR-INFIX":
                operator_flg = True
            else:
                operator_flg = False

            if current_criteria_pos:
                if t.tsubtype == "ARG" and t.tlevel == current_criteria_pos[-1]:
                    current_criteria_pos.pop()

            if not current_criteria_pos:
                criteria_flg = False

            if t.tcriteria:
                list_obj.append(FormulaTokens(t.tid, "LHS", "", "", t.tlevel, t.tcriteria))
                current_criteria_pos.append(t.tlevel)
                criteria_flg = True

            if t.tcriteria or criteria_flg:
                if operator_flg:
                    list_obj.append(t)
                    list_obj.append(FormulaTokens(t.tid, "RHS", "", "", t.tlevel, t.tcriteria))
                else:
                    t.tlevel += 1
                    list_obj.append(t)
            else:
                list_obj.append(t)

    return list_obj


def get_formula_token_list(input_formula):
    tok = Tokenizer(input_formula)

    output = input_formula + "\n"

    lid = 0
    indent = 1
    token_list = []
    criteria_pos_list = []
    criteria_flg = False

    if tok:
        for t in tok.items:

            if t.subtype == "CLOSE":
                indent -= 1

            lid += 1
            lvalue = t.value
            ltype = t.type
            lsubtype = t.subtype
            llevel = indent
            lcriteria = criteria_flg
            token_list.append(FormulaTokens(lid, lvalue, ltype, lsubtype, llevel, lcriteria))

            if t.subtype == "OPEN":
                indent += 1

            if t.value in function_with_criteria.keys():
                criteria_pos_list.append(lid + 1)
                criteria_flg = True
            else:
                criteria_flg = False

        if criteria_pos_list:
            final_token_list = token_list_update(token_list)
        else:
            final_token_list = token_list

        for obj in final_token_list:
            output += "    " * obj.tlevel \
                      + "|__" \
                      + str(obj.tid) + "|" \
                      + str(obj.tvalue) + "|" \
                      + str(obj.ttype) + "|" \
                      + str(obj.tsubtype) + "|" \
                      + str(obj.tlevel) + "|" \
                      + str(obj.tcriteria) + "|" \
                      + "\n"

        return output
