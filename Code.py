def Jhas_optimality_criterion(matrix):
    M = len(matrix)
    
    marked_entries = []
    used_rows = set()
    used_cols = set()
    
    for i in range(M):
        max_val = -999999
        max_row = -1
        max_col = -1
        
        for r in range(M):
            if r in used_rows:
                continue
            for c in range(M):
                if c in used_cols:
                    continue
                if matrix[r][c] > max_val:
                    max_val = matrix[r][c]
                    max_row = r
                    max_col = c
        
        marked_entries.append((max_row, max_col, max_val))
        used_rows.add(max_row)
        used_cols.add(max_col)
    
    while True:
        row_to_col = {}
        col_to_row = {}
        
        for row, col, val in marked_entries:
            row_to_col[row] = col
            col_to_row[col] = row
        
        swap_happened = False
        
        for current_row in range(M):
            current_col = row_to_col[current_row]
            current_val = matrix[current_row][current_col]
            
            best_profit = 0
            best_col = -1
            
            for k in range(M):
                if k == current_col:
                    continue
                
                candidate_val = matrix[current_row][k]
                if candidate_val >= current_val:
                    gain = candidate_val - current_val
                    displaced_row = col_to_row[k]
                    loss = (matrix[displaced_row][k] -
                            matrix[displaced_row][current_col])
                    profit = gain - loss
                    
                    if profit > best_profit:
                        best_profit = profit
                        best_col = k
            
            if best_profit > 0:
                displaced_row = col_to_row[best_col]
                row_to_col[current_row] = best_col
                row_to_col[displaced_row] = current_col
                col_to_row[current_col] = displaced_row
                col_to_row[best_col] = current_row
                swap_happened = True
        
        if not swap_happened:
            break
    
    marked_entries = []
    for row in range(M):
        col = row_to_col[row]
        val = matrix[row][col]
        marked_entries.append((row, col, val))
    
    return marked_entries
