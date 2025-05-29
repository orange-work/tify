'use client'
import type { FC } from 'react'
import { useRouter } from 'next/navigation'
import React, { useEffect } from 'react'
import { useTranslation } from 'react-i18next'
import { useAppContext } from '@/context/app-context'
import useDocumentTitle from '@/hooks/use-document-title'

const ApiOrchestrationPage: FC = () => {
  const router = useRouter()
  const { isCurrentWorkspaceDatasetOperator } = useAppContext()
  const { t } = useTranslation()
  useDocumentTitle(t('common.menus.apiOrchestration'))

  useEffect(() => {
    if (isCurrentWorkspaceDatasetOperator)
      return router.replace('/datasets')
  }, [isCurrentWorkspaceDatasetOperator, router])

  return (
    <div className='p-4 text-gray-500'>
      API Orchestration Page
    </div>
  )
}

export default React.memo(ApiOrchestrationPage)
