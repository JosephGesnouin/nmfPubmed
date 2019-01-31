###Definition tfidf ####

term.frequency=function(row){ ###Calcul TF
  row/sum(row)
}

inverse.doc.frequency=function(col){ ####Calcul IDF
  corpus.size=length(col)
  doc.count=length(which(col > 0))
  
  log10(corpus.size/(1+doc.count))
}

tf.idf=function(tf,idf){
  tf * idf
}
